#!/usr/bin/python


class ToastXRaspberry(object):
    def apply(self, upper_limit, layer_count):
        if upper_limit >= layer_count:
            return 1
        return layer_count / upper_limit + 1

