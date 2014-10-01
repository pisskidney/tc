#!/usr/bin/python


class ToastXRaspberry(object):
    def apply(self, upper_limit, layer_count):
        if upper_limit >= layer_count:
            return 1
        return layer_count / upper_limit + 1 if layer_count % upper_limit != 0 else layer_count / upper_limit


class ToastXToast(object):
    def bake(self, u, c):
        if max(u) > max(c):
            return -1
        elif min(c) < min(u):
            return -1
        elif max(u) < min(c):
            return 1
        elif min(len(u), len(c)) == 1:
            return 1
        else:
            return 2

