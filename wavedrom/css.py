# The MIT License (MIT)
#
# Copyright (c) 2011-2018 Aliaksei Chapyzhenka
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Translated to Python from original file:
# https://github.com/drom/wavedrom/blob/master/src/WaveDrom.js
#

import attrdict
css = attrdict.AttrDict({})
css.default = """
text{font-size:11pt;
    font-style:normal;
    font-variant:normal;
    font-weight:normal;
    font-stretch:normal;
    text-align:center;
    fill-opacity:1;
    font-family:Helvetica}
.muted{fill:#aaa}
.warning{fill:#f6b900}
.error{fill:#f60000}
.info{fill:#0041c4}
.success{fill:#00ab00}
.h1{font-size:33pt;font-weight:bold}
.h2{font-size:27pt;font-weight:bold}
.h3{font-size:20pt;font-weight:bold}
.h4{font-size:14pt;font-weight:bold}
.h5{font-size:11pt;font-weight:bold}
.h6{font-size:8pt;font-weight:bold}
.s1{fill:none;
    stroke:#000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.s2{fill:none;
    stroke:#000;
    stroke-width:0.5;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.s3{color:#000;
    fill:none;
    stroke:#000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:1,3;
    stroke-dashoffset:0;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s4{color:#000;
    fill:none;
    stroke:#000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none;
    stroke-dashoffset:0;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible}
.s5{fill:#fff;stroke:none}
.s6{color:#000;
    fill:#ffffb4;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s7{color:#000;
    fill:#ffe0b9;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s8{color:#000;
    fill:#b9e0ff;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s9{fill:#000;
    fill-opacity:1;
    stroke:none}
    .s10{color:#000;
    fill:#fff;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s11{fill:#0041c4;fill-opacity:1;stroke:none}
.s12{fill:none;
    stroke:#0041c4;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
"""

css.narrow = """
text{font-size:11pt;
    font-style:normal;
    font-variant:normal;
    font-weight:normal;
    font-stretch:normal;
    text-align:center;
    fill-opacity:1;
    font-family:Helvetica}
.muted{fill:#aaa}
.warning{fill:#f6b900}
.error{fill:#f60000}
.info{fill:#0041c4}
.success{fill:#00ab00}
.h1{font-size:33pt;font-weight:bold}
.h2{font-size:27pt;font-weight:bold}
.h3{font-size:20pt;font-weight:bold}
.h4{font-size:14pt;font-weight:bold}
.h5{font-size:11pt;font-weight:bold}
.h6{font-size:8pt;font-weight:bold}
.s1{fill:none;
    stroke:#000000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.s2{fill:none;
    stroke:#000000;
    stroke-width:0.5;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.s3{color:#000000;
    fill:none;
    stroke:#000000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:1, 3;
    stroke-dashoffset:0;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s4{color:#000000;
    fill:none;
    stroke:#000000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none;
    stroke-dashoffset:0;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible}
.s5{fill:#ffffff;stroke:none}
.s6{color:#000000;
    fill:#ffffb4;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s7{color:#000000;
    fill:#ffe0b9;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s8{color:#000000;
    fill:#b9e0ff;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
.s9{fill:#000000;fill-opacity:1;stroke:none}
.s10{color:#000000;
    fill:#ffffff;
    fill-opacity:1;
    fill-rule:nonzero;
    stroke:none;
    stroke-width:1px;
    marker:none;
    visibility:visible;
    display:inline;
    overflow:visible;
    enable-background:accumulate}
"""
