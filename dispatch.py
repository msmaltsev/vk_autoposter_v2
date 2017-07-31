# !usr/env/bin python3
# -*- coding: utf8 -*-

import os, shutil
from sendDispatch import *

class Dispatch:

    def checkContent(self, name):
        if name in os.listdir('dispatches'):
            if 'photos' in os.listdir('dispatches/%s'%name):
                print('photos folder OK')
            else:
                print('creating photos folder for dispatch %s'%name)
                os.mkdir('dispatches/%s/photos'%name)

        else:
            print('creating folder for dispatch %s'%name)
            os.mkdir('dispatches/%s'%name)
            print('creating photos folder for dispatch %s'%name)
            os.mkdir('dispatches/%s/photos'%name)
        print('folder OK')
        return 'dispatches/%s'%name


    def __init__(self, name):
        self.name = name
        self.attachments = {'photos':[]}
        self.folder = self.checkContent(name)


    def addText(self, text):
        f = open('%s/text.txt'%self.folder, 'w', encoding='utf8')
        f.write(text)
        f.close()


    def addLinks(self, links):
        f = open('%s/links.txt'%self.folder, 'w', encoding='utf8')
        f.write(links)
        f.close()


    def dispatchAsDict(self):
        d = {}
        d['name'] = self.name
        d['text'] = open('%s/text.txt'%self.folder, encoding='utf8').read()
        d['links'] = open('%s/links.txt'%self.folder, encoding='utf8').read().split('\n')
        ph = os.listdir('%s/photos'%self.folder)
        ph = ['%s/photos/%s'%(self.folder, i) for i in ph]
        d['photos'] = ph
        return d


if __name__ == '__main__':
    d = Dispatch('test_dispatch_2')
    # d.addText('тестовый текст рассылки')
    print(d.dispatchAsDict())
