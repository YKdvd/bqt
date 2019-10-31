"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
import AppKit
import bpy
import objc
from pathlib import Path

from PySide2.QtGui import QIcon
from PySide2.QtCore import QObject

from bqt import BlenderApplication

# GLOBALS ###
SETTINGS_KEY_GEOMETRY = 'Geometry'
SETTINGS_KEY_MAXIMIZED = 'IsMaximized'
SETTINGS_KEY_FULL_SCREEN = 'IsFullScreen'
SETTINGS_WINDOW_GROUP_NAME = 'MainWindow'


class DarwinBlenderApplication(BlenderApplication):
    """
    Darwin (MACOS) Implementation of BlenderApplication
    """
    def __on_focus_object_changed(self, focus_object: QObject):
        """

        Args:
            focus_object: Object to track focus event

        Returns: None

        """
        return NotImplementedError

    def __get_application_hwnd(self):
        """
        This finds the blender application window and collects the
        handler window ID

        Returns int: Handler Window ID
        """
        ns_window = AppKit.NSApp.mainWindow()
        ns_window.setSharingType_(AppKit.NSWindowSharingReadWrite)
        return objc.pyobjc_id(ns_window.contentView())

    def __get_application_icon(self):
        """
        This finds the running blender process, extracts the blender icon from the blender.exe file on disk and saves it to the user's temp folder.
        It then creates a QIcon with that data and returns it.

        Returns QIcon: Application Icon
        """
        blender_path = bpy.app.binary_path
        contents_path = Path(blender_path).resolve().parent.parent
        icon_path = contents_path / "Resources" / "blender icon.icns"
        return QIcon(str(icon_path))