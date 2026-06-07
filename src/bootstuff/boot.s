; this is the bootloader of trenex
; enjoy ig
format binary
org 0x07C00
use16

boot_start:
 mov ax, 0x3000
 mov ss, ax
 mov ax, 0xFFFF
 mov ss, ax

boot_build_msg: db "Trenex 0"
