from hashlib import sha256
from PyQt5.QtCore import QObject, QEvent, QMimeData, QUrl, pyqtSlot, \
    pyqtSignal, QThread
from fbs_runtime.application_context import ApplicationContext, \
    cached_property
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDragLeaveEvent, QDropEvent
from PyQt5.QtWidgets import QMainWindow, QWidget
from tutorial.ui.hasher import Ui_WidgetHasher
import os


class AppContext(ApplicationContext):

    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        result = QMainWindow()
        hasher = WidgetHasher()
        result.setCentralWidget(hasher)
        return result

    @cached_property
    def image(self):
        return QPixmap(self.get_resource('success.jpg'))


class WidgetHasher(QWidget, Ui_WidgetHasher):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.reset()
        self.hash_thread = None
        self.current_fingerprint = None
        self.current_filepath = None

        # Intercept drag & drop events from button
        self.button_dropzone.installEventFilter(self)

    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.DragEnter:
            print('DragEnter')
            self.on_drag_enter(obj, event)
        elif event.type() == QEvent.DragLeave:
            print('DragLeave')
            self.on_drag_leave(obj, event)
        elif event.type() == QEvent.Drop:
            print('Drop')
            self.on_drop(obj, event)
        return QWidget.eventFilter(self, obj, event)

    def on_drag_enter(self, obj: QObject, event: QDragEnterEvent):
        mimedata = event.mimeData()
        assert isinstance(mimedata, QMimeData)

        if mimedata.hasUrls():
            if len(mimedata.urls()) > 1:
                return self.reject_drag(event, 'One file at a time please. Try again!')
            url = mimedata.urls()[0]
            assert isinstance(url, QUrl)

            if not url.isValid():
                return self.reject_drag(event, 'Invalid URL. Try again!')
            if not url.isLocalFile():
                return self.reject_drag(event, 'Only local files are supported. Try again!')
            if os.path.isdir(url.toLocalFile()):
                return self.reject_drag(event, 'Directories not supported. Try again!')

            event.accept()
            self.button_dropzone.setStyleSheet(
                'QPushButton:enabled {background-color: #0183ea; color: white;}'
            )
            self.button_dropzone.setText('Just drop it :)')

    def on_drop(self, obj: QObject, event: QDropEvent):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.process_file(file_path)

    def on_drag_leave(self, obj: QObject, event: QDragLeaveEvent):
        self.button_dropzone.setText('Drop your file here or click to choose.')
        self.button_dropzone.style().polish(self.button_dropzone)

    def reject_drag(self, event, message):
        self.button_dropzone.setText(message)
        self.button_dropzone.setStyleSheet(
            'QPushButton:enabled {background-color: red; color: white;}'
        )
        event.ignore()

    def process_file(self, file_path):
        self.current_filepath = file_path
        self.button_dropzone.setText("Current File: %s" % os.path.basename(file_path))
        self.gbox_processing_status.setEnabled(True)
        self.progress_bar.setMaximum(os.path.getsize(file_path))
        self.progress_bar.setValue(0)
        self.progress_bar.show()
        self.label_processing_status.setText('Calculating fingerprint ...')
        self.hash_thread = Hasher(file_path)
        self.hash_thread.hashing_progress.connect(self.progress_bar.setValue)
        self.hash_thread.finished.connect(self.hash_thread_finished)
        self.hash_thread.start()

    @pyqtSlot()
    def hash_thread_finished(self):
        self.current_fingerprint = self.hash_thread.result
        self.progress_bar.hide()
        self.label_processing_status.setText('SHA256: %s' % self.current_fingerprint)

    @pyqtSlot()
    def reset(self):
        self.current_fingerprint = None
        self.current_filepath = None

        # Dropzone
        self.gbox_dropzone.setEnabled(True)
        self.button_dropzone.setEnabled(True)
        self.button_dropzone.setText('Drop your file here or click to choose.')

        # Processing Status
        self.gbox_processing_status.show()
        self.gbox_processing_status.setDisabled(True)
        self.label_processing_status.setText('Waiting for file to process')
        self.progress_bar.hide()


class Hasher(QThread):

    #: emits num bytes processed
    hashing_progress = pyqtSignal(int)

    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path
        self.result = None

    def run(self):
        hasher = sha256()
        progress = 0
        with open(self.file_path, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                else:
                    hasher.update(chunk)
                    progress += len(chunk)
                    self.hashing_progress.emit(progress)
        self.result = hasher.hexdigest()
