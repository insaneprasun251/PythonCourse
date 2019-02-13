import rpyc
from plumbum import SshMachine, BaseRemoteMachine


class Draw():
    def __init__(self,
                 user=1,
                 function="enter_win_nbrs",
                 product=8,
                 action=1,
                 draw=1,
                 set_number=1,
                 win_numbers='"1234567|"',
                 win_plus='"',
                 win_power='"',
                 win_super='"',
                 win_promo='"',
                 greenball=0,
                 multiplier=0):
        self.user = user
        self.function = function
        self.product = product
        self.action = action
        self.draw = draw
        self.set_number = set_number
        self.win_numbers = win_numbers
        self.win_plus = win_plus
        self.win_power = win_power
        self.win_super = win_super
        self.win_promo = win_promo
        self.greenball = greenball
        self.multiplier = multiplier

    # def prepare_rpc(self):
    #     return "$USEC/bin/rpc -t {} -p {} {} {} {} {} {} {} {} {} {} {} {}".format(self.user,
    #                                                                                self.function,
    #                                                                                self.product,
    #                                                                                self.action,
    #                                                                                self.draw,
    #                                                                                self.set_number,
    #                                                                                self.win_numbers,
    #                                                                                self.win_plus,
    #                                                                                self.win_power,
    #                                                                                self.win_super,
    #                                                                                self.win_promo,
    #                                                                                self.greenball,
    #                                                                                self.multiplier)

@keyword
def process_draw():
    draw = Draw()
    # SSHLibrary.library.SSHClient.write(text="lala")
    rem = SshMachine('xxmkt1055.gtk.gtech.com', user='root')  # "10.17.20.187"
    conn = rpyc.classic.ssh_connect(rem, remote_port=22)
    conn.execute(print("$USEC/bin/rpc -t {} -p {} {} {} {} {} {} {} {} {} {} {} {}".format(draw.user,
                                                                                           draw.product,
                                                                                           draw.function,
                                                                                           draw.action,
                                                                                           draw.draw,
                                                                                           draw.set_number,
                                                                                           draw.win_numbers,
                                                                                           draw.win_plus,
                                                                                           draw.win_power,
                                                                                           draw.win_super,
                                                                                           draw.win_promo,
                                                                                           draw.greenball,
                                                                                           draw.multiplier)))


process_draw()
