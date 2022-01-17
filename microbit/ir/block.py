def on_ir_datagram():
    global Button1
    Button1 = convert_to_text(makerbit.ir_datagram())
    if Button1 == "0x00000000":
        basic.show_icon(IconNames.NO)
    else:
        basic.show_string(convert_to_text(makerbit.ir_datagram()))
        basic.pause(1000)
makerbit.on_ir_datagram(on_ir_datagram)

Button1 = ""
makerbit.connect_ir_receiver(DigitalPin.P1, IrProtocol.NEC)
basic.show_leds("""
    . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
""")
basic.pause(1000)
basic.clear_screen()
