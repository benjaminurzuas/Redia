# Genera index.html (la app instalable) a partir de la misma página publicada en Claude.
import sys, re
src = open(sys.argv[1]).read()
title, rest = re.match(r'(<title>.*?</title>)\s*(.*)', src, re.S).groups()
rest = rest.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title}
<meta name="description" content="Planifica tu semana: universidad, gimnasio, vida y finanzas.">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Redia">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/favicon.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
out = head + rest.replace('<header class="top wrap">', '</head>\n<body>\n<header class="top wrap">', 1) + '\n</body>\n</html>\n'
open('index.html', 'w').write(out)
