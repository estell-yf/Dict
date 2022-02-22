{\rtf1\ansi\ansicpg936\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;\red193\green193\blue193;\red34\green34\blue34;\red88\green196\blue193;
\red234\green121\blue57;\red191\green131\blue194;\red109\green188\blue135;}
{\*\expandedcolortbl;;\cssrgb\c80000\c80000\c80000;\cssrgb\c17647\c17647\c17647;\cssrgb\c40392\c80392\c80000;
\cssrgb\c94118\c55294\c28627;\cssrgb\c80000\c60000\c80392;\cssrgb\c49412\c77647\c60000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # coding\cf4 \strokec4 =\cf2 \strokec2 utf\cf4 \strokec4 -\cf5 \strokec5 8\cf2 \strokec2 \
\pard\pardeftab720\sl360\partightenfactor0
\cf6 \strokec6 import\cf2 \strokec2  base64\
\
\pard\pardeftab720\sl360\partightenfactor0
\cf7 \strokec7 '''\
input_select = str(input("
\f1 \'c7\'eb\'ca\'e4\'c8\'eb\'c4\'e3\'d2\'aa\'d1\'a1\'d4\'f1\'b5\'c4\'b9\'a6\'c4\'dc
\f0 \\n1.
\f1 \'b1\'e0\'c2\'eb
\f0 \\n2.
\f1 \'bd\'e2\'c2\'eb
\f0 \\n"))\
if input_select == '\cf5 \strokec5 1\cf7 \strokec7 ':\
    file = str(input("
\f1 \'c7\'eb\'ca\'e4\'c8\'eb\'c4\'e3\'d2\'aa\'b1\'e0\'c2\'eb\'b5\'c4\'d7\'d6\'b7\'fb\'b4\'ae
\f0 \\n"))\
    es = base64.b64encode(file.encode("utf-8")).decode("utf-8")\
    print(es)\
elif input_select == '\cf5 \strokec5 2\cf7 \strokec7 ':\
    file2 = str(input("
\f1 \'c7\'eb\'ca\'e4\'c8\'eb\'c4\'e3\'d2\'aa\'bd\'e2\'c2\'eb\'b5\'c4\'d7\'d6\'b7\'fb\'b4\'ae
\f0 \\n"))\
    ds = base64.b64decode(file2.encode("utf-8")).decode("utf-8")\
    print(ds)\
'''\cf2 \strokec2 \
input_select \cf4 \strokec4 =\cf2 \strokec2  \cf5 \strokec5 str\cf2 \strokec2 (\cf5 \strokec5 input\cf2 \strokec2 (\cf7 \strokec7 "
\f1 \'c7\'eb\'ca\'e4\'c8\'eb\'c4\'e3\'d2\'aa\'d1\'a1\'d4\'f1\'b5\'c4\'b9\'a6\'c4\'dc
\f0 \\n1.
\f1 \'b1\'e0\'c2\'eb
\f0 \\n2.
\f1 \'bd\'e2\'c2\'eb
\f0 \\n"\cf2 \strokec2 ))\
f1 \cf4 \strokec4 =\cf2 \strokec2  \cf5 \strokec5 open\cf2 \strokec2 (\cf7 \strokec7 'base_encode.txt'\cf2 \strokec2 , \cf7 \strokec7 'r'\cf2 \strokec2 )\
str1 \cf4 \strokec4 =\cf2 \strokec2  f1.\cf5 \strokec5 readlines\cf2 \strokec2 ()\
\pard\pardeftab720\sl360\partightenfactor0
\cf6 \strokec6 for\cf2 \strokec2  i in str1:\
    \cf6 \strokec6 if\cf2 \strokec2  input_select \cf4 \strokec4 ==\cf2 \strokec2  \cf7 \strokec7 '1'\cf2 \strokec2 :\
        es \cf4 \strokec4 =\cf2 \strokec2  base64.\cf5 \strokec5 b64encode\cf2 \strokec2 (i.\cf5 \strokec5 encode\cf2 \strokec2 (\cf7 \strokec7 "utf-8"\cf2 \strokec2 )).\cf5 \strokec5 decode\cf2 \strokec2 (\cf7 \strokec7 "utf-8"\cf2 \strokec2 )\
        \cf5 \strokec5 print\cf2 \strokec2 (es)\
    elif input_select \cf4 \strokec4 ==\cf2 \strokec2  \cf7 \strokec7 '2'\cf2 \strokec2 :\
        ds \cf4 \strokec4 =\cf2 \strokec2  base64.\cf5 \strokec5 b64decode\cf2 \strokec2 (i.\cf5 \strokec5 encode\cf2 \strokec2 (\cf7 \strokec7 "utf-8"\cf2 \strokec2 )).\cf5 \strokec5 decode\cf2 \strokec2 (\cf7 \strokec7 "utf-8"\cf2 \strokec2 )\
        \cf5 \strokec5 print\cf2 \strokec2 (ds)\
}