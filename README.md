# dssc2017-3d1p

This is the GIT repository for group 3D1P, at UCL DSSC 2017

```html
<head><meta charset="utf-8" />
<title>DSSC_MSFT</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.6 (http://getbootstrap.com)
 * Copyright 2011-2015 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
@-moz-document url-prefix() {
  div.inner_cell {
    overflow-x: hidden;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 20ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">equity</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;Equity.csv&quot;</span><span class="p">)</span>
<span class="n">apple</span> <span class="o">=</span> <span class="n">equity</span><span class="p">[</span><span class="n">equity</span><span class="p">[</span><span class="s2">&quot;Ticker&quot;</span><span class="p">]</span><span class="o">==</span><span class="s2">&quot;AAPL US Equity&quot;</span><span class="p">]</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">simplefilter</span><span class="p">(</span><span class="s1">&#39;ignore&#39;</span><span class="p">,</span> <span class="ne">ImportWarning</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Determine whether a market is in an upward trend or downward trend at the moment is not challenging, but predicting the length of a trend is a bigger challenge.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;Close&quot;</span><span class="p">]</span><span class="o">+</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;Open&quot;</span><span class="p">])</span><span class="o">/</span><span class="mi">2</span>
<span class="n">apple</span><span class="p">[</span><span class="s2">&quot;5avg&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">rolling_mean</span><span class="p">(</span><span class="n">apple</span><span class="p">[</span><span class="s1">&#39;avg&#39;</span><span class="p">],</span><span class="n">window</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span><span class="n">center</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span><span class="n">min_periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">apple</span><span class="p">[</span><span class="s2">&quot;30avg&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">rolling_mean</span><span class="p">(</span><span class="n">apple</span><span class="p">[</span><span class="s1">&#39;avg&#39;</span><span class="p">],</span><span class="n">window</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span><span class="n">center</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span><span class="n">min_periods</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">apple</span><span class="p">[</span><span class="s2">&quot;30avg&quot;</span><span class="p">]</span><span class="o">-</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;5avg&quot;</span><span class="p">]</span>
<span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff_norm&quot;</span><span class="p">]</span><span class="o">=</span><span class="p">(</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff&quot;</span><span class="p">]</span><span class="o">-</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span><span class="o">/</span><span class="p">(</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span><span class="o">-</span><span class="n">apple</span><span class="p">[</span><span class="s2">&quot;avg_diff&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">())</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">apple</span><span class="p">[[</span><span class="s1">&#39;5avg&#39;</span><span class="p">,</span><span class="s1">&#39;30avg&#39;</span><span class="p">,</span><span class="s2">&quot;avg&quot;</span><span class="p">]][:</span><span class="mi">100</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
wFdKKaXcwP8D1/y/dEXGmusAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Mean reversion is a known trading strategy and probably one of the easiest way to start algorithmic trading. Even though it is quite easy to calculate the 5 days and the 30 days rolling averages of a stock price these values give more insight than just the direction of the trend. Larger difference between the two mean values indicate steeper price changes, therefore we calculated the daily difference between the two rolling averages and normalized it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[60]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;5 days average prediction - 506153734175476c4f62416c57734963.faa6ba63383c4086ba587abf26b85814.v1-default-1643 - Results dataset.csv&quot;</span><span class="p">,</span><span class="n">header</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
<span class="c1">#plt.plot(data[&quot;APPL Label 1&quot;][:200]-data[&quot;Scored Labels&quot;][:200], color=&quot;blue&quot;)</span>
<span class="c1">#plt.show()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[57]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 1&quot;</span><span class="p">],</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels&quot;</span><span class="p">],</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 1&quot;</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">poly1d</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 1&quot;</span><span class="p">],</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels&quot;</span><span class="p">],</span> <span class="mi">1</span><span class="p">))(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 1&quot;</span><span class="p">])),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Our model predicts the rolling average difference at any particular day for the next 5 days. The larger the difference becomes the quicker the trend is and vice-versa. With this indicator traders can get an quickly insight whether the market faces a flash crash or a longer term. The plot above shows the prediction for the next day against the actual difference. Clearly our model captures the relationship.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[58]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">f</span><span class="p">,</span> <span class="p">((</span><span class="n">ax1</span><span class="p">,</span> <span class="n">ax2</span><span class="p">),</span> <span class="p">(</span><span class="n">ax3</span><span class="p">,</span> <span class="n">ax4</span><span class="p">))</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">sharex</span><span class="o">=</span><span class="s1">&#39;col&#39;</span><span class="p">,</span> <span class="n">sharey</span><span class="o">=</span><span class="s1">&#39;row&#39;</span><span class="p">)</span>
<span class="n">ax1</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 2&quot;</span><span class="p">],</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (2)&quot;</span><span class="p">],</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">ax1</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 2&quot;</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">poly1d</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 2&quot;</span><span class="p">],</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (2)&quot;</span><span class="p">],</span> <span class="mi">1</span><span class="p">))(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 2&quot;</span><span class="p">])),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">)</span>
<span class="n">ax2</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 3&quot;</span><span class="p">],</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (3)&quot;</span><span class="p">],</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">ax2</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 3&quot;</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">poly1d</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 3&quot;</span><span class="p">],</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (3)&quot;</span><span class="p">],</span> <span class="mi">1</span><span class="p">))(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 3&quot;</span><span class="p">])),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">)</span>
<span class="n">ax3</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 4&quot;</span><span class="p">],</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (2) (2)&quot;</span><span class="p">],</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">ax3</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 4&quot;</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">poly1d</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 4&quot;</span><span class="p">],</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (2) (2)&quot;</span><span class="p">],</span> <span class="mi">1</span><span class="p">))(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 4&quot;</span><span class="p">])),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">)</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 5&quot;</span><span class="p">],</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (3) (2)&quot;</span><span class="p">],</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">ax4</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 5&quot;</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">poly1d</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 5&quot;</span><span class="p">],</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;Scored Labels (3) (2)&quot;</span><span class="p">],</span> <span class="mi">1</span><span class="p">))(</span><span class="n">np</span><span class="o">.</span><span class="n">unique</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;APPL Label 5&quot;</span><span class="p">])),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;r&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhcAAAFkCAYAAACThxm6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAAPYQAAD2EBqD+naQAAIABJREFUeJzsvXt4VeWZ8P179vmU0w4hJ5JwCiGcBQQVBRXP1TJFRa22
Vq0ztnbs5TfTr9OvzttO32vq205bO5232lbHikpRHFEUQS0gp5SDgBwTQgIh5+wkO9k72ee91nq+
P1YSARMESSDI+l2Xl2Tttfa+9+F51n2+hZQSAwMDAwMDA4PBwnShBTAwMDAwMDD4cmEoFwYGBgYG
BgaDiqFcGBgYGBgYGAwqhnJhYGBgYGBgMKgYyoWBgYGBgYHBoGIoFwYGBgYGBgaDiqFcGBgYGBgY
GAwqhnJhYGBgYGBgMKgYyoWBgYGBgYHBoGIoFwYGBgYGBgaDypArF0KIx4UQNUKIqBBiuxDi8s85
/34hxF4hRFgI0SSE+G8hhHeo5TQwMDAwMDAYHIZUuRBC3AP8GvgJcBmwD/hACDFigPPnAUuB54FJ
wF3AHOBPQymngYGBgYGBweAhhnJwmRBiO7BDSvn9nr8FUA/8Tkr5y37O/yfgMSll8QnHvgf8v1LK
wiET1MDAwMDAwGDQGDLPhRDCCswC1vcek7omsw64coDLtgEFQohbe54jG7gbeG+o5DQwMDAwMDAY
XCxD+NwjADPgO+W4Dyjp7wIp5d+EEA8ArwshHD3yvQN8b6AXEUJkAjcDx4HYuYttYHBJ4wBGAx9I
Kf0XWJYBMda9gcGgMSRrfiiVi7NGCDEJ+E/gp8CHQC7wK+CPwLcHuOxmYNn5kM/A4BLifuAvF1qI
02CsewODwWVQ1/xQKhftgApkn3I8G2gZ4Jp/AcqklL/p+fugEOK7wBYhxI+llKd6QUC3XHj11Vcp
LS09d6kHgSeffJJnnnnmQosBGLIMhCFL/1RUVPDAAw9Az7oaxhyH4bPuh9N3OJxkgeEljyHLZxmq
NT9kyoWUMimE2A0sRA9t9CZ0LgR+N8BlLiBxyjENkIAY4JoYQGlpKTNnzjxXsQeFtLQ0Q5Z+MGTp
n+EkywkM91DDsFr3w+k7HE6ywPCSx5DltAzqmh/qPhe/AR4VQnxTCDER+AO6AvESgBDiaSHE0hPO
fxe4UwjxmBBiTE9p6n+iV5wM5O0wMDAwMDAwGEYMac6FlHJFT0+Ln6GHQ/YCN0sp23pOyQEKTjh/
qRDCAzyOnmsRQK82+ZehlNPAwMDAwMBg8BjyhE4p5bPAswM89lA/x34P/H6o5TIwMDAwMDAYGozZ
IkPAfffdd6FF6MOQpX8MWQwGk+H0HQ4nWWB4yWPIcv4Y0g6d5wMhxExg9+7du4dbcoyBwUXHnj17
mDVrFsAsKeWeCy3PQBjr3sBgcBiqNT+s+lwYGBgYGBiciN/vp6OjA6/XS2Zm5oUWx+AMMZQLAwMD
A4NhRzQaZcWKlZSVVREKgccD8+YVs2TJYpxO54UWz+BzMHIuDAwMDAyGHStWrGTVqgbM5sUUFj6J
2byYVasaWLFi5YUWzeAMGHLlQgjxuBCiRggRFUJsF0Jc/jnn24QQ/y6EOC6EiAkhjgkhvjXUchoY
GBgYDA/8fj9lZVVkZ99KdvY0HI40srOnkZ19K2VlVfj9w3bsjUEPQ6pcCCHuAX4N/AS4DNgHfNDT
+2Ig3gCuAx4CJgD3AZVDKaeBgYGBwfCho6ODUAjS0opOOp6WVkQopD9uMLwZ6pyLJ4E/SilfBhBC
PAZ8BXgY+OWpJwshbgGuAcZKKQM9h+uGWEYDAwMDg2GE1+vF44FgsBaHY1rf8WCwFo9Hf9xgeDNk
ngshhBWYhd5hEwCp172uA64c4LI7gF3AD4UQDUKISiHEf/SMXzcwMDAwuATIzMxk3rxifL61+Hz7
icWC+Hz78fnWMm9esVE1chEwlJ6LEYAZOHWSqQ8oGeCaseieixjwdz3P8RzgBR4ZGjENDAwMDIYb
S5YsBlZSVraSujq9WmTRouKe4wbDneFWimpCn4L6dSllCEAI8f8AbwghviuljA904ZNPPklaWtpJ
x+67774vfRc0A4MvyvLly1m+fPlJx4LB4AWS5othrPsvL06nkwcfvJ/bbzf6XAwW53PND1mHzp6w
SAS4U0r5zgnHXwLSpJRf6+eal4CrpJQTTjg2ETgETJBSHu3nGqNTn4HBIGF06DQwuDBcqGZhF12H
TillUgixG1gIvAMghBA9f/9ugMvKgLuEEC4pZaTnWAm6N6NhqGQ1MDAwMDC4EHxZm4UNdZ+L3wCP
CiG+2eOB+APgAl4CEEI8LYRYesL5fwH8wJ+FEKVCiPnoVSX/fbqQiIGBgYHBpYvf76eq6uLsf/F5
zcIu1vc2pDkXUsoVPT0tfgZkA3uBm6WUbT2n5AAFJ5wfFkLcCPwX8DG6ovE68K9DKaeBgYGBwYXj
i4YELnar/9NmYYvJztZLbntLbzdtep1Q6A/s29dyUb63IU/olFI+Czw7wGMP9XPsCHDzUMtlYGBg
YHBhOVfloNfqz85eTGFhEcFgLStWvI3P9yyPPPKtYZ8A2tssrLDws83CNm6spKFBMG7ckr73tmrV
WmAlDz54/4UR+CwYbtUiBgbnxLkkRQ336YvDXT4Dg7OlP+XgTG+gp1r9yWSS5mY4diyfysq3OHjQ
x9y5Y5k/fx55eXnDcs0M1CzM59tHIBBn4sQ7PuPRKCtbye23+4fl+zkRQ7kwGFZcCPfo5117oW/q
F7vr18CgP04XEjiTG+ipVv+hQxVUVnbhcMxHyioqK/PZsmU7r7yyjmnTpgzLNdPbLExXqHSPRTBY
S2Pju6SnZ5KTM/Gk89PSiqir09+7oVwYfKkZrBvvULhHz9QCGujaROI1bDbbBb+pn8t7MzAYrpwu
JHC6G2jvngP0Wf2aNp76+g7c7lLARywWRtPG4nROIRb7kK6uq1i2bDOh0FIef/yx8/H2zpj+m4WN
Y/du+0Xd/txQLgy+EINtTQ+mexR0CygajbJmzWtcddUciouLz+pagGXLfobbPY3CwvN/Uz9xAz0X
687gy82F9qqdC2c7P6R3z1m/fh+dnVEyMpzY7WEaG1fjdl9NNBrCbq8jFPorkEZq6mysViv19W9z
4EAricQY/uu/3gLg4YcfvGAejFO/s4GahS1duuwzHg2fby2LFl0c7c+HXLkQQjwO/DN6Zcg+4B+l
lB+fwXXzgI3AASml0SVnmDGY1vRgu0eTySSHDlVw/HgbnZ21PPXU77jttiv6VXxOvDYS8RONduB0
erHZUqivjzNnzrXn9aZ+qtKmqn5qa7uZNy/vpPMuJveoweAzGMr9hVZMTg0J2GwptLYepKvrY5Ys
KfmMTK+++hp/+MOHRCIjECIFKbtxOFqZMUNBVbtIJI4A+RQVTaa5eRYORxoNDdsIhWKMGDGLlBQv
fv9+Vq06isdz/r1+n/edZWZmnvSeL/b250OqXJwwcv3vgZ3oU1I/EEJMkFK2n+a6NGAp+pCz7KGU
8VLmi24u56oMnMqZukcHkvdUC6g39iqEm4yMElyuW1m1ahv9KT5erxeHI8nOnc8SDMZJJMBmA6u1
GyktjBxZfFqZBptTlTafbx8tLb9hz56NLFhwV995F5N71GDwORflfjjl8CxZsphE4jWWLfsZ9fVx
wEZBgYNkcgzRaLRPHr/fz7Jl79HZOQGv914cjiJisVo6Ol6jpuYIzz//z6xc+Q6bNwfJyrqM9vY2
2tq2EAh8QEbGdNLTSwmF9pOamkF+/vWUlW04716/s/3OLvb258Nq5PoJ/AFYht6Zc9EQy3jJca6b
yxeJlZ5OkTmde9RiidDS0sKHH64fsN77RAsoGo1y/HgbQriRciejR0+hqGg+Pl96v4pPZmYmZnOA
w4ebSU//Bqmpk+jqKqex8XnS07tJJNqA3JNkGqqben9KW1HRfMaOLaOmZjVFRQXk5Ey86NyjBoPL
uSr3g+F1HCyvh9PpxGaz4XZPY86caxk5sphEoo01a9ZitX4qz9GjR6mvj5OW9jU8Hv29ejzTUNU4
DQ3/RmdnJ0888V1yclZSVrYWh6MGn68Js9lLRsb9hEL7CYfXUlJSTHb2dOrqNnxuTsdg3szP5Ts7
1aNxsTBkysUJI9d/3ntMSimFEKcbuY4Q4iFgDHA/RvOsIeFcN5eziZWeiSLTX8a031/Jnj3PkJJi
4gc/+G9aWgKMHTuXyy57iEik9TPy9roQ16x5jc7OWjIyShg9egqTJy/ue87+FB+/34+qZlBSch1d
XYJwuAKnU1BauhhVXUZd3dt91w/1TX0gpU1/z98jGn2Nurq0i849ajC4fNFESDh3xWSwvR698hQW
fipPrzL/WXlsQPopz5Dec/xTS3/hwgZeeulV3nmni8OHfVRX/xCvN5WpU7/C5MmL6eioOm1OR+97
s1giTJ6czf3338OoUaPO+r2d+B737NmD3x+nuPjsv7OLlWE1cl0IUYyujFwtpdT0USQGg8lghDQG
Kp/q78Z7porMqfHFpqaDQDYFBfdz4EAHLpeb5uadpKauZ8aM+0+SF/TFefvtt3DVVXN46qnf4XLd
SlHR/L7nH8jj0NHRQSxmYe7cG9E0a58r1mRKcuzYJ8ye7aa6+vzEPAdS2iKRVqZNm8IPfnB/33lf
to3I4Mw520TIEzkXxQQGv3LpTOUZN24cBQUOamvLMJtTcTjSiMWCBAJlFBU5GTduXJ/H4cMP17Nn
j2DWrH8jLa2DiorDSHkUTVPo6Kga0EDofW+ZmbcRDO7j2LH9bNiwg7Vr9/DQQ7edtQJ1orLi90c4
dKiCjo6/MmPG1ShKN06nl+7uxi9teHPYVIsIIUzooZCfnDD91NAuBplz3Vx6OZNko7NRZJxOJ7ff
fgulpcUEg0FeeSWG2/11LJZ8VPUAXu8VhEKpVFW9QUFBPWlpRdTUKLzwwkscPdp9khV1440zWbNm
Gz5f+ud6HE7cqLOzp+FyuQDw+faTnm7lkUe+1fe59RKJRIYkNv15SttAFS8GlxZno9yfyrkoJoOd
a9WfPJFIhGg0Snd3NR6Pfk5VVRVer5cHHriB5577mHBYJRLJRkofXu8eliyZz+rV7590E8/NfZDR
o0czfnw2VquHmhorlZVvkZlZxaJF0z9jIJz43pqbD3DsWAdu96M4HE58vs2sWHGUsw0bvfDCS2ze
HKSw8C6Ki4tob/9PPvnk9xw+/A4ZGaOQshuXq53HHrvpS2ksDKVy0Q6ofDYhMxto6ef8FGA2MEMI
8fueYyb0YaoJ4CYp5caBXuzJJ58kLS3tpGP33Xcf99133xeT/kvKuWwuJ3ImyUa9ikxWVgp+fxVO
pxeXK/MziszpKiTMZicWi0ZDwzGiUSvxeJANGzYxcqQDVT3K5s3FFBbedZIVdeutI1m0aNQZZVmf
yUYdjUb7Nq9zcQWfSSz3fGaIL1++nOXLl590LBgMDvrrDCWX6rr/or+Tc1FMBssw6U+eN99czeHD
R+jsdBAO+0gkNjNmTDNPP50kGExisUS54opivvOd2WzeXEln5yFcLsmsWWOJx+OsWxcgLe16LJYO
YrEg5eVhamr+SkpKJjYbjBo1Dqt1PN/73l3MmTNnwPeWlZVCfX0VbvdiPJ5pKEoMRRlHamrxGSWB
floue4Cysipstjys1gN4vcWkphZgtY4hGp1ASkopZnM7sIfz6aA/n2t+OI1c7wKmnHLsceA64E7g
+Ole75lnnmHmTKNi9fM4l81loOcb6Bqn00lT00E++eQ3gAeTKUZRUQn5+TNPUmROdLVmZWVRX7+L
xsY/9VVICBHF76/CYrFis6WQTHqoqHiL9PR6Jk/+0WesqI8/XsnTT/8jt99+y0k3c7/fT0NDQ598
vcc/b6M+W1fwqUrE2cSpz2eGeH834T179jBr1qwheb2h4FJd9+fyO/miislgGSb9ybN16z+zf/9O
rNYi3G4XZnM65eUR6uv34nAUk0iY2LFjAzfemM//+l9P8uabqzh0yMeOHe0cOLCvJ1TSTSyWoL29
AkUZi6JcT3b2RFQ1QnX1WoqK2hg3btxJr31iPxmLJcbRo9uIRBQyM3UFKhYLYrPByJHFtLUNnATa
S+9eYbffht3ehd2eTWXlBhKJpfh8LYwa9R1isQCzZ48lNzeX7u7L2blzJQsWVPV9xqf9HtvaICvr
C33OcH7X/FCHRX4DvNSjZPSWop40ch3Ik1I+KKWUQPmJFwshWoGYlLJiiOW8pDhf1vH69ZsIBkfS
1jYaTStEygB1dR+RmfkKP/7xt/tu+GVlVWRm3kFzM9TXV5JIpKCquRw48BpZWZkoikJqaifh8EZs
thApKS683ix8viA228kL7UQrqrj4U8/D0qXL2LSpnPLySgKBOOnpmUyaNIpZs0Yxf/48br/9ls8o
I3DmrmC/3095eTnr1n1ETU0IRXH1KRHJZII1a1pPGa70P7S0PMu3v93/cKWLNUPc4PzyRX4nX1Qx
+aKGyed57CKRCEJkcd119+Dx5JJMwvvvLyUUstDZGSU1NYrXOxuH41bWrXuNePxpQqEJZGc/gMOR
QjD4NOFwkhEjZpCdPQ/4Cap6kFjMSzI5CpOpDSGOAPG+1zzRw9DeHiMYbMLvryMYrCEaFYTD2xkx
YirR6DFKSrwkEm1nFTZKSRnPkSM7EaIQt/tWamv/jKZZsVgcmExJ0tPTcblcqOpIysoO8tRTz2I2
p/VveLS1wcqVsGIFbNwI+/fD5Mmf+31daIbVyHWD80N/mwtAQ0PDoFnKvQstLW0BLS0ekslchPAg
ZSqh0POEwyHgU3dkMBjj2LEobncpaWlpmEyZ1Nc/SmXlLwkGnWRllTB9+hUUFc0jJSWPeLyL1auf
oLW1ioyM05eKvvjiUlatOko06qCjYwYWyzza26Ns23aMjz46/eyBz3MFNzU1sXLlOyxb9h7l5e2E
wybS0lKYNu0m3O7LWbFiNeHwUUpLf9gzXCnaE9Pt5PDhQxw61MbChVOH3cwDgy8/X0QxWbhwAT7f
6xw8+BeCQceAhonf76epqYnNm8s+d2T4p2tsOg5HGlu3/gG/P4Km3YvZnMRsHklHx1ZSUhJo2lS2
bv2Q+fP/nuzsafj99agqWK13E4+7SCY1nM47kXIrqrqcUOgIKSluSkvH4HaLPs/DsmWv8dxzu+ju
nk4gYCcczsHpdJCba8bvb6Kt7Y8oyjwmT56Fzebn6NH13HBDxmk/mxP3CofDRUGBl8rKKhyObBIJ
CAZ3E41mkpZWwt/+doCCAi+BwDv4fB4mTry3r8x81aq12EIvc5/DAq+/Dhs26C9w/fXwxz/COVSu
nE+G3cj1Ux7/N+DfhkIuA31zcblcQ9JQp6OjA78/TiDgJjt7OiZTKoqiIMRVdHdvYdu2I3zjG368
Xi8WS4xjxw7jdt+Ox6On6FitkoyMUtzuNrKyrBQUnFz90d3dSE4ONDe/CQRJScknmQwRDG5j0SI9
8fHAgQOsXfshL764kUQil66uw3g8D5KdfTUNDdtpbx/FiBFjCATW0N5ezLJlewmFunn88cf6nV/Q
nyt48+YyXnxxE21t41DVb+JwFBGJfML+/R/jcKSTmno5hw8fYvp03cNy6NBKKisbcDi+iRA+ksnU
ARt8GRgMFz5bpqkxfXrKZ8o0Tzxv//7jn1tCDieHWzQtn7a2BiyW60gkcrBYAihKEbFYmO7uFdhs
WVitKiZTr/EQw+FwEg7nEo+3oKoJpFSxWG4iNdXH3Lk3kZs7k+7uRlS1Ea/Xi9/v5+WXP6S2dh5S
ziQcNgGziEQyCQY3sGjRr9i9+0Vqat6gvPxD4vEgVmuS9vbx7NxZy3XXTTqpffhAe8XkyaVABZWV
mwkGd6Io4HA04PVei6Z52bPnAyKRjUyd+hijR8/FEQtwRfMexu9ZTenbf0MKEAsWwO9/D4sXn1M4
5EIwbKpFDC4MQzUUy+v1IkSYhoZKpMwmFmtAVSUmUwMOR4jq6ihNTU1MnTqVKVOy+OijLTgc01AU
B6FQOceP/wJFidHSksDhaKKi4kfMn/9jiorm9fXAcDic1NdXs3fvDsxm2eO2LSAcTudHP/ov9u8/
SEODnWRyPiNHXkEg8D90dXloadlHOBwlmTTT0REnFjuMz1eOzTaCmpqD7NjxMRZLDrGYFY8HpGyj
qekd4GRX8MKFOezYcYxIZASpqYuJxbJxOEahKDkkEio1NQeYO3cJkKC1tQq73UZ9fRV2+x0kkyOw
WoOMGDGZ9nZYv37NWWXbX+jWzQaXFv3tEzt2rCUnZ9NJ+8SnOQfXEwi0YbE4qK3dhsPxNnPm6APD
Tq0sOTHcEghMIpnUcDgsdHV9gKY5UdVMVDUPVTUDCrFYO1u2rGHJku/idHrJykpD046TSERJJKrx
eEKEQsdIS7Pi9Y6nu7vxpNDNzp07OXzYTzI5Hbt9NCZTFyZTDslkEr9/FdFogHg8lXBYI5kMoqqF
KMq1VFen0NjYwu7d29m79wC/+MX/5t13155kmEnZRmPjakDfK3JzIRKpITU1jeLiHxIKNVBT8w7h
sIbJdJxUkjxobuTK5XcwvvoDTJpCTcGVvDzzZhb87inGXnVV32d7sa15Q7m4hBmK0rJeXC4Xzc0H
6eysQtPCQBYQQU+/CdDWZmbz5jKmTp3K179+D2vWbKO19WUUJZPm5m3EYrnY7XegquuIxzsIBn28
++4PGT16JB6PHRiD1TofszmN7GwzicQWRo60sH+/j/37N1Jc/BCBQBcOx02EQjGCwSBWawrJJHR2
+ohE2lHVbIRoR1XdmEwPk0jY8Pl28f77R5gyxcOcOd/F59vH0aNv4PXuIxwOneQKnjlzGu+/fwgh
UnC7x2E2h1CUGBZLGolENtHoIbq7GykosNPVtZHjx/00N7cRi4VQlFpstg7efTeIw2FFUY7wwgsv
8cQT3z2txyja1cWmn/8C1m6kIjWfitJJw3KUtMGXh7PJO9q0qYLOzhm0tHRRW9sBZGEy5REIvAvA
6NHzaW72c/So3m2g1+KfOXMaoVA3ZWUbaG3dSCSyDSEsKEoSRXkfKMVsTuBy2YHRNDVtZd26DEpK
pmAyBdG0N5g48Q4mTRpPNNpMefkmUlJ8tLUtxWKJccUVWSxcuADQqyNisTBWq8RuTyMSCSGEhtkc
RVGiHDq0hmPHAlitd2K1+lHVa4lELNjtZoTIxWabyl//+gdisR8QDk84SeFqanqH7OxGVPXTfLYb
bsjgb3+bhM2WRyLhxqmaub57C7eFKrgmtB/H+s3UFVzFhzf9ivLSO6mO+lHVlXy1RG8HNZzatZ8N
hnJxCTMUpWW9vPjiUhoa8rDZmojFNgOj0bu5e0gkNOx2lX37WvD7/YwaNYq7776BN944gNXqpaEh
C4djEdHoq2iaDViAqtoJhyupqjqIzVbNmDFfpanJics1hfT0UQQCdtrblxON5hCNdtLR8Qnt7X4c
jkzMZo3W1v2YTF0kk++haSPRNDt2uwNF2YTTeSUpKX9HV1c1sVgDXu9UOjt388knr3L48GE6OwNA
PaWlXdxxx3UsWvQVHA4HABkZTqTsRlWbSEvLpr29g2RSRcomIExX18fcf/9XsNls/OlPywgGm7HZ
JuF0FhCPFxEIZJGa6sPjyWfz5iA5Of14jBoaYO1aWLsW89q13BKL0eX0krzqDo6YbzPGrxsMKWe6
T3R0dFBe3kBHx9XEYjZUNR1IQVWL0LRMdu1azd69a7FYEjz22I+w2zNQVSddXQHS0+1MmlSCqrYh
xChU9Vrc7vmEQu1o2rvADqxWQU7OzaSkfJvDhx9h376fcfBgFiaTDY8nAiwnEDhIerqVJ564iquu
msPKle+wZ4+fLVvCHDz4OxYunM7YsYU4HDHi8TWoajoWiyQc3gVswmyO0dRUj6qWkpLiIRr1oSiT
MJvNSFmJokjc7hKSyTzKyir6cj/gU4VLVVfy7W/fRjAYJCcnh82by6gtP8QI38/4h8hRblb34JBx
9jlK+XdXPjuL5jN2wQ8HTJAdKu/yUGMoF5cwQ1Va5vf72by5ErP5cpzO4ySTU5EyH00TCNGMzRbB
ZDqM3x+hqamJ1avfZ/fuBrq7/TQ2vkoo1IXN5kTTosAjqOo0IASkoqophEKtHDjQhcmk4XIpuN1v
oaqNdHfXkUjUIWUNHR0JhAiRSOxCVd2oqoYQs5DyPWA9kEI8PgKrNYHD8VMCgTYikTCqaqKry0sw
WEltrQ9F+Ttstgmo6kYaGvbzwgvvsm7dAfLyivF4wG4P43C009HxGh7PIlwu6OzchtW6mbw8E0uW
zGfJksVEIhHWr9+Hqo6mra2ZYNCBwzEfVfXT1fVXpky5jMLC2boleFMzmYcP9ykUHDwIJhPJ2bNZ
M/lKykf/A8nJdyOFqa+JjDF+3WCoOJt9IhDwI6VKMNiEqu5G04JAnGSyAkVJRYg0HI5u/P4CVHUi
dnsOeXlj8fu3sWlTLQ0Nh1CU24DZRCJmhMgCFmA2t+F0ppGZeQtNTa+jKE5MpmvJyVmMy1VAKLSb
UGgbs2d7eeQRvQLr+ef/zIoVu06aonro0GoeeOAqSkoKKS8/QEfHv5BICKTsBlrRtADhcAghFDo7
vSQSR9G05zGbH0dRYjidAk1rxWYThEJupEzF7/fjdDpxuVy4XHmUldXw61+/gkOmUnhoC9c0Hedv
XS04tSSfmMfztONx1ntn40+pY+TIOELsJxzuP0F2KL3LQ42hXFzCDHbPi146OjqIx/VW2qFQF6o6
FkgFJJrWQizmor29A0hh8+YyPvywne5uN4oyFoslDSn3Eo9vwmy+AVWdBDgAO5CLqvrR5wmkomkl
hEJvEYlILJYb0LRJSFkHWBFiMlJmoCgH0bQx6GEZD0J4gRyEEGjaVajqYTo6dmAyTcZmU1BVB4ri
IxxuQ4gbsVonoCjd2GxehJiL338Um20O06cvIZHQczFmzFCoqTlCbe1PAQuTJlm44465fOtbD/Ql
uzU0NKAoLubNe4x9+5axZ89bqOpRhJA4HCZKPcXMq/mIgkOvk/GXX0E4DNnZcMst8NRTcOONHPf7
WfGTZRRpMVRqAAAgAElEQVQW3oJDmPo+7y/zfAKDC8Op8f0TBwPabCNJJFrp6tr4mX0iPd1OdfX/
0N2tIkQBQtyIlCFgPIryHmBFyjzM5ntR1Qyi0SCKMoJk8hqamzeQTHqRshiTaSyqGkEvLExFVd2E
QrUcO/YLQqEmhBiJ3b4Ai8WFEIK0tOuIx1UOHqzqk//EKapmcx7h8FHa2layatUmFi++jkOH/kgi
MRIhZiHEGKRsQ9PeIhTKxGq9GUWZjBCHgfWo6q+BEjRNEI8fxOtNJRjsZNu2LdjtE7DZoKDAS8i/
nynHDvNIWyqX1W/DkQxzyJrFn/Pm8nLMynHzXBIJDVPsI+ZMu4LS0ttobv4D3/vebWRkZHwmn2Io
vctDzZArF0KIx4F/Ri873Qf8o5Ty4wHO/RrwHWAG+t3kEPBTKeWHQy3nxciJWcrwxWZODFbPixM3
I6/XSyDQSDTqIJnsBBqAG4BOwIWUjQSDBzGbJ7FvXwvd3Xaam0243fcyenQRXV2r6O5ehqZVIGU1
UAyE0UfVBNAbtx5BD7P40bT5JBJtmEwW9KFHV6Io24HvAoeBXYAfKa0IkY/d/hiathxNa8Fk8qBp
G7DZnJjNVqxWP+HwNqQEKUsRwoqmdZJMqnR3K1gs44BMNM3WZ0nE4yu49dZiNm3aS1dXgvz8bAoK
CvodCx+JtDJz5rfwN9dR7Ovmmu7j3JDcS+kb/4GK4NjIfGLf/z6uO++EGTPA9KkS4ZVySDxNBga9
69fpdLJ+/abPxPdvuOFatm79OVu2/G+iURtOZ4Jrrinijjse7XsOr9fL2LEFHDu2G9DQtDkIoSJE
GlJOQ+9EMAmzGYSYgaI0YTIlaG09gsmUh6KYkTIV6EDTjgBKz3+HgXqSSQ9dXT6krCCRgFgsQjDo
RAgNq9WLxzOBpqYuOjo66OzspL4+jseziI6OMIHAWmAUUk5l//51jBrlJhq1IUQmmtaA7hmdCkxA
VSegqlYslgg22yxisXakfBmzeQdSjiUzczzhcDV2uxtFOY7bOpHLWw9wfcWr3BLdRSoKPjGFD2d8
h1/VhjiQiKME6jCbJalOC7m5i4jFGhk37moiEX22yLhx4/rdu4fKu3w+GFLlQghxD/Br4O/5tInW
B0KICVLK9n4umQ98CPwI/S7yMPCuEGKOlHLfUMp6MdGb4NNfU6gFC0rPKtHnXDtC9pdsVFhop7b2
UM+4ctBHxuxHH5LbihDlmExJ2tpiNDXV4POl43Z/s2+Ucl7e9VRVHUXTVgN/Ab4CjEdXUsoAD/r8
u63oPdk6gZFoWgHgBpLABvRGsHejd5b/EZCBlGZisecRoh2HIxWTKU48fgBFqUBVMzGbU3pkBCm3
omlT8XgKEWI0XV1v4HarOJ0pfZ9vWloRGzbUsHNnEFUdgxAp+P3dVFevJpFI8OijerV1ZmYmN03M
oP2Vn3JFIMBP6rbi1pK0iHS2uK/l+bSHWatUc/Ud6Tz/7//e72c9VJ4mg0uXU9dvU1MV3d0aM2c+
SWFhSV/Dt/feW0M4PI4rr7wHq9VDMhnC79/Gu++u7Yv7Z2ZmMn36KDZsOIzZnNFj+U8A7OiTG9KB
kT3exBeAKJqWoKsrgD5GqhuYCGzs+XsBulFxFAhjMoHVeiXd3evQtFL0fWEaUjYSj68jHt/M/v01
vPLKcubMmUkiodLc/EtisRD65NRWIImUsHJlNfH4OKR8uOe1dgJNQBqQj8lkQdOqMZnayMgoIJnM
IjMzjWTSz4gRLuwmC/d5b6T4k2VcV/Mr0klSgZtncLG98HHsl91LKLSVXd1rUNV8YAwWS5jW1q0k
k3Gys+fT3V3dr/fnRC7mNT/UnosngT9KKV8GEEI8hv6LeBj45aknSymfPOXQj4UQi4A70L0eBnya
4BMIePqaQnV0xKmpCREInN2AnV6+aEfIE5ONcnPz2LNnI2+88R+Ew/mYTDcAVvTO7tuBbZhM43A6
x6EoXnbvrkZRBIlEMQ5HjMzM43R0dBAOB5AyDd1T8Qkge16tDn2TMKFvVE8CH6BvDuMRIhUpI+ib
hAOoAV7uuXYy8HV0p9gBpFyKojQwatQtBINHsNmuJTPzVszmVOrr64hEVqOqO7FaxwBmNK0WVd2G
lC7GjBnTN+CspeUw9fWHsdmuJyvrGzgcRcRitXR0vMaKV97hVpsJ9+bNpJSVcVdlJZrJRNWIXJ5N
HcOHlilUuXJxe7w4HILctCmoagi/f+A46vmcPWLw5efU1vuffLKGePwobW1VjBw5lebmA1RVtdPS
0khOjgertZ7JkxdjtTo5ftzOmjWvcdVVc/qG6t1//z28+eZm/P4QJlMEIQQmUxxNM6F7IEKo6nEg
iK74j0X3aLyHbjDUAM3Ax0AFuqFgBm5Fyr10dXUipRu4Ar0vYxYwCl0J+R1dXd08//zHLF++nubm
w6jqAuAR9FtdI/p+EiUaXdDz73XArehKzY6e5/FhtV6Nph3FbFYYOXIELtc8Jo6fQanvJb6VqCNt
x0ZSEq9RbUrjOfMkXpcODkgnmkxi91WRvv0VEolPgBlIeRtmczouV5JQaCkdHW+Tl1eLzVZ6Rmv3
Yl3zQ6ZcCCGs6Kbqz3uPSSmlEGIdcOUZPodANzs7Pu/cS4VPO19eT23tBlJT9QE7oZCPrq4KiooK
KCtbe0aJPudaN90rS2rqrVgs+VRU1NDY6ETTShGiBIdjIYnEYaQsQYgspPwAq/VypGwmmUzFZLoD
q7WNWGwv4XAN4bCCvpFE0b0T+UAE2I8Q45EyG5gDvAvMRIhrkHId+kZUipRxdEVmH3ANkIm+oZSj
/wyvRFdUJgNLSCZ/Rzj8AWlpGqrahcPhxmz2YjJtx2wGs7kBTXuBri4bUnZhtR4nL28BWVlJYrEg
Pt8+ystfIpm0kpOzBI9nGtmxWuZ2/Y3L/JuZU7MN95a38dvd/G3UWCIPf5uCh79FUyTC5t+9z5jc
hxktw0gJXu84TCYLdXXPnDaOej5njxh8uTk1WdDv92OxjMPhmEZ9/XskEkupqQliNn8dqMJsLqSy
chequgKz+TKqq5vp7KziBz/4JV/72rUsWbKYzMxMxoxJYe/ewwjxDiZTEoslE0V5CykzgenACPQZ
lXFgD7pxcBV6CKQQfQ/4GvrtqR49Qu5CyjJ0JSQNXbkwoysmDnoNECGKkPIrNDXVo2kB4EZ0xaER
uB1dmVmK7gktAFaj7zUxoBZ93mYATStBURRi4RbGHH+Zb9hrufXgr0hPhFFHj+YvWfk81zGDSscT
dIc6UdU2EBUIulHVqQSDe4jHm0hN/REm0ygsliRCeHG5bkGIA/zTPy3i5ptvPqO1e7Gu+aH0XIxA
//Z9pxz3ASVn+Bw/QPdzrxhEuS5qehN8PB4PiYTuJgNwONIIBsFmG0kodPpEn4HqphcuXEBTUxMw
cAywF7/fz7Zt29izpwpFmU083k1bWysOB1itOahqNqpahxDbkbIFKS1ALfH4s0ASk+nvcLkWIGU6
DseviEbfQp9bNxb9Z1kDzAXGAP8Xp/NrRCJZwF/RwyD0bDbTgVXAm+ibUwZQCoxDn3V3I/oQXgf6
RtWOHkrJBTqJRkOYzUWYzc20t/8Mt7sEj+c4yeQxFGUm+flfBUx0dx9mxIhyrrjChqquZONGPRzl
NKlcGY7y1aNPc6NSwejoYVTM7LIV8rS5mF0jbueIczbh7uOoq3Yx9sCvGD9+HFVVZRw5EsFmy+5J
BismK6v4jOOoxuwRgy9Kr1HR2dl5UrKg0+nEZgNNSycSiVBbW4nb/RCK4sVmq8NuH4/FksW+fX8i
HteIxyOARnm5pKbmbRoa6klPT6ezswibLUQ4vAdV/YRkUiBEBIvlHhTFgxB1SDkdPQxSjp5TNQk4
iG5Lgu7lGImuSBSiGw2geyw1dA/mLHQvhwIkAEEyKQkEQMoRmEy5qGoRn3o+9R4Z+v4SRt9vPkAP
t0bR95wJCOq4Sv01S0Q7i9UmclSF+qSTspLxlPzr/4ecOZP/+41/4WDnPBxiBJrmx2S6FilHYTav
Qgg7ilKAlLsJh9vwevPJycnDbDaTTI4nGs1i/PjxgzokcjgybKtFhBBfB/4V+OoA+RkncamMXu5N
8EkmQ9hsEIvV4vFM65vel0i0fu4N6tS6ab+/kt/+9tc8/fSfSSbTgAQFBXbuv/8rPPDAvSflbzQ0
NLBs2escOuTj0KEKjhzpJiUlSXb2lSjKPoLBIyQSR9Bv3pU9DbS+hr5RbER3RVZhNtcghIrFYsds
/nui0Z8Db6N7JlJ6zr8OfdOwE48fwWzWUNXDQBSzuRpVzUeI2UgZQIhKpMwC7kG3Qnp7a1wGvA68
gRBjkVL05FPsAUbgcNyM2z0eKd1IuZPc3AzGj7+Xd955ikhkDGazHZfLwqRJC8nKmo8Q73J5VoIZ
wTDXhENM8u3BnozQFKtli+dqXij5VzZZx7HzyP9BE1NJTc4mEY4QjxdjMuXR1FSGzTaZlpZGLBaN
goL70bQA+/e/RUbGap544vbztoEYI9cvLT7bwjtCU1Mjbnc1+fmzcLn0eRj79pVhNjdjNmejqk7i
8eMUFqYRjdajql7a27swmRqxWiN4vYtIJCbQ3LyCZ55ZTkpKFh0d6UQiQXRFIA50IKUDVZVAA1L6
gWPo69OGriw0oiv9VwN+9PWrJ1jq3o2t6OHOu9EVglU9zz0S3eOwtuc5xqMo1Ug5Eyk70UOpxehK
SB16jUAIPdxyDN3+DSHYxhVEuYcd3EUj+VqSJrOHrQVXcnT2P7C6tYK29n2Mf3U72svvEY2a8XpT
6e4+hJRhIIbVOhZFMQEWXK6bCYU2IEQ5nZ2jiURi2O0a8DcmTbJ/Zjrr+eJLMXId3URUoa8Uv5ds
dFNyQIQQ9wJ/Au6SUn50Ji92qYxe/jTBZxtpaXYaGt4hEvGjKHHy80N0dR09baJPVVUVa9ZsJy3t
7r5qh7a2KhoaRhKLzWT06NuwWGLU1b3FH/7wIYlEnJtuWtiXRf7nP6+hujqJy5VBNGrG45lDV9cm
4vGPice7SSQiaFoNQrSgux5vQrc83sJsDiDlSDSthWRyB+3tf4/ZXIDJNAF9kQfRPRfXoZeuZgIf
AR2o6vvolk4rUISq7gbKkbIJszkHVa1EV1xC6M6uVEymsWjaAXTLJAcp5yLENPTioz2AQihUSTLp
Q1GuxGzOJZncjNvtxWSyc/nlVzBx4lQ8VhNjG7YyevvbTDz+NgWhDlRhpr5wHlvm/yurkgqvHWoh
qYxipOYi0f0BqtqJ1VqE1TqdWKwai2UsqtpFR8cGPB5Bbu4jRKOr0LRyNC0Nu30cKSm1fV0EzwfG
yPWLky8azuyvGVN399Ps2fMiFouVtLQisrKSeL0f43AEaGkJEIttpqTkckpKZlFZWcXevRtIJA6R
kmIhO3shmjaPYNCEzXYf8Xg54XAbsVgGsBgh5vb0j1gOrEHKzeieiA7gFeBa9Jt8C/rabUV3as8A
3kdXMhrRc6xa0dd1fc+72d5zXTb6vtHY8++5SBlGiNVoWjfwDvpesgtdmQihKyXvAxEup5F7WM/d
VFNIlGZhZpV1JNsLFxKcdBOTptzFoUMraW4x092dS3W1iUTCSWtrNampzWRk5JFMRlGUGJrWjqqG
cLkmIkQXTqeTZPIIUo4gkfBgMoUQYhPjxo24YB6IL8XIdSllsmfU+kL0b7g3h2Ihehp/vwgh7gNe
AO6RUr4/VPJdzPQm+GzaVE4kUkkgsB2vN5MxYwqYNWsUM2dO+0xSYK/VsmbNLrZvbyI9/X06O+sZ
M2YBNTUVaNqNWK1WnM48XK5MhLDQ3PwMv/3tSjZsOEZLSwUdHW4UZS5ZWbeTTDbT3PwsGRlO7PYG
urs1LJar0bRUdGXiAFLuRI+tLgcEqno3ujXzW/RNRaCqoKrd6KGMVvTqED96DFag/3QS6BtECN2V
ORvIQ99Q1qNpEpttHInEcfRNZBIQRtOOo5esSmA0QrQh5V/RPSNLgO1Eo3NQlKM4HA2YTFfQ3v4O
9fUvc3V+KrcEVzPz3Z8zoWELDjVGizmDTU4nO4uuIHb173HnTcTlcpGajDLH8yrl5SsZNaoGkylM
S0sHLlc+ZrMHMGO15gLNKEqCWMxOTs5ULJatzJkzBocjH5OphLa2eqLR6JD8Zgwufs62DfSJSgjQ
bzOmmTOfpKrqlyc1cXriiatYuPBH/OUvr7NpUyO5uZcjRILcXGhrO0Z3t0Je3mOkpl7GsWONWCyS
ZDJCPN5NMhmlN7wpZajHS6ih5z3MRM+j6kT3Yv4n+rrPAy5HD2luR1//HuD6nuu2o4c/J6Anbxai
eznb0T0fSeA2YBSatg6zeRqKshHd87EdPTF0Yo9cqcykiSWsZQnNjCGCjxTeFFnsGZ/JhIfuZceu
GlJT72N60XwiET/19VVEIgrxeCoOx32MGDGeWOyXBAJ7GTXKg9ebQmvrelS1ApPJgt3ehsXyN1JS
ZmCxjCYcriYaPUJubiF5ebMR4vRJ218Whjos8hvgpR4lo7cU1QW8BCCEeBrIk1I+2PP313seewL4
WAjR6/WISim7MAA+m+ADEIvF+sYbl5W9+ZmNp9dqSU29l4yMNhIJN5WVOwmFXicaVXus5yRWq75J
BQJOgkEbJpOXhgaoqIiQSKQgxMdkZ1sxmy0kk9DSsg2TyYTFsgi3ezrxeBualoeUAqhEd0MmgW+i
uyeXoVsgj/UcV9ATMhvQrZo29DLS1egWiaXnuqye84uBiQgRRspGoBApJ2M2X4fZfBRVXYoeu70T
XZEpBA4hRAQhgkjpRN/gTMBuhCgFShHxN7jZup4brU3cXNVAfihAEsFO6xietixia8Zcjrmb0WQd
/vZ63H9dz6hRXRQUeJk8uZTCwrlkZlbxve/dRTAYZP/+p4jHt6IoGUCIZHIbqroFi8WLw+Ghq6sc
pxMyMvJxuTLx+fYP+7p1gwvLmbaB7lVC1q8/QGdnkowMK1OmZBEIJBk79uRmTJmZJYTDU/pt4vSP
//hdsrNXsn79X2hoSJCRYePrX5/Aa6810tBQTjyu0dX1NqoaIZlsR9NC6B7IEnRF4A2k3IauBFwH
FKErEx70cMZz6IbAfegpegF0r8ZG9CqzevRciDr0io7eKhI3ek6Vv+f6cejhzzBSPoui+NBvM350
76eZaeRzD/tYwi7G00YbHt4kgxXMYbvNzeRpSV588VdMnTqVpUuXsWrVNny+dFRVobOziXBYJSPj
AdLTdQu/qOifUdUfoijvMXXqJPz+WpLJEK2tVlyutRQWTqe5eQwZGQsIhXaSTL7B9dc/gds98nOT
tr8sDKlyIaVcIYQYAfwM3We1F7hZ6m3XQG+sVXDCJY+i/zp/3/NfL0vRy1cNTuDEBJ+lS5exZk0r
qanXM3JkMYlEW9/Gc/vtt5xktQQC+6ms7EKIObS0rEJVQyjKJ6Snz8JkstPY2ERT0yFUNUZray1t
bU4U5UY07Uqghfr6l7BYcrBaHyAWO4iUlcTjLmKxA0hpR/8KMwAnsAX9Zu5D3xwOoFsZs4AqdKvF
ge6sKkHfJKzoEbUd6D+RR3vOO9DzPHU9zbWOo4deKohG69GrQK5At1RmI0Rhz4yPFHS3qwWTyYMQ
6UADhWoLX+E9bklu41rKcHcotNpS2OJJ5ePi2exMncjeY0dJJlNQw6sxRa0IMRpV7SQQWIHbnUt3
d4xg8AgZGUdZtGg6c+bMwe/3U1IymoqKNlT1TUymZuLxACbTGLzeGYwYEeLYsbfIySnGZLLg8+2/
KOrWDS4cZ9MGetmy13juuV1EIjMRIhspfezfv5PUVB+Zmf03Yzp9AreGrthb8HhSuPPOq/ntb/9C
fX2IeDwPKaeg38yz0D2Fq9BLwFX0tZeKbhR40W85Y9BDE9k9x0TP9TZ0BaS358U16MaBhh7SkMAt
PdfXoSdxH0E3JBLooRYvehJ3hMl8zBIquYd2StiFHycruYzv8BAfMQ9NLMNutzBr1ggefXQOU6dO
BU4u/fT7I0AVdvsYcnOn930iyWSC3NyvMmrUOr7//a/0heZeeOElNm8OkpV1Ge3tbXR0bEPKnZSU
XEFmZvElZUQMeUKnlPJZ4NkBHnvolL+vG2p5vkz0uj1jsRh//vMafL7rsVg0bLZKCgq8ZGXdwPr1
b+B22/H74xQX61bL5MmlQAXHj9fR2VlHTk4YVQ0jZRq1tTY6O5t7JhE2oGkeNG0in2Zup6BpOSQS
U1EUJ2BFVQOAhpSpCJGPlM3oi96EnnNRix7S6EDfBMb0/LsT/SeY1fP/GLoy8VV0r8Pv+LSwqLcs
tRj95zQCWIxuER0BtqFne49HL0WtR8qJ6IqKFSlbsckDLMDMrSzjVnZRQoCkNLOVQv6NLNZg4qjI
QOkSpAkTWWaw2814PPkEAlnE4zOw273AURTlXZqbf4HL5UVVLdx11919deeZmZk8+OAtPPfcLrq7
81GUQiKRnShKOfn5nUyYUERpqRNVDVFX98xFU7ducOE40zbQfr+fV19dR0fHjWRm3orDkUYsFsTv
NxOLvUpKyv/0XXdqM6aqqiqOHz/O6NGjKS4u5sUXl7JqVQNe7w3k5o4gmQyxatU20tOP4fHk0tbW
1VORoQ/p08lGb3Q3GfgG+jp9oefxQvQ13qs89CotQXQDI4xucNT1nFuO3nyvAn39fw19/Y9GX9cz
ex7/GN1Dup0SpnMP77OEMiYTJICLt5jG97mS9cRQ0LDbR+O0ViFlK7m5Vu6775qT1t6pnuGVK0fy
3HNbCQb34fVeSSwWJByuIicnRl5eOjNnzuxTzJ544rvk5KykrGwtDkcNgUCQsWPnMm7cwkvOiBi2
1SIGA3Nq7LW6ehvV1RYKCuaRkjKaWCxIRcURamqaCYePUF/fSG1tCz7fGhYsuAur1cqMGdNIT48S
jRbx1FMPs2PHLv70p3c4dOgFFEVBb8Gb0tOwJgX9p1KNbj040Vtg16J7KbzoN/SxSGlD91AcQV/8
S4DXgN3oN/5kz/PoMz70zWgDugsT9E3Jg66Y5KEnd7Wju0dT0TeeELAIfUPq7rkmE73/Re/GtQco
YiyN3MoebmU/17EZFxr12Hif8fyIO1lHLt0cRPeIFEO8ESEEqno54bCNcLgNKT/Bbv8xkUg7iYQF
k+kGTKYMVPUNolENIY4RDvdurjr3338vVqutxzWdICMjj8mTpzF58kRKSkooLi4+5z4jBpcOZ9oG
+ujRo9TXx0hPn4fHo0eVPR4HqjqPYHAVs2dbaG4+uRnTDTdcy6OPPs6WLXVEozYcjhgjRoRpabER
Co1GVf8Hh8NJ1v/P3plHyVFf9/5T1fsy+z6SZqQZ7UILAolFQpIRBgbLZrEtEctL8BLbAcchie2s
J+cl8XOe48R5kDj2s81iGzAChCWERgiEFiQkoX0ZLbPve3dPT+9dXVXvj1s9I4FYjWyDdM/pM9PV
VdXV3XXv73u/dyvJw+vN8OqrDbjdN6Pru1AUH4qyCtP0IyDhaUQHFyI6OYIAgzPW9nLGm1dpSBWI
E3E4epAEbhcyMcJEunM2Ig6KG3FO+pHS1BIgwlS+y2pGWUOEebzGKG42UMZ3+DIv8hnSHGB8qduM
onSQl5ckP9/H17++invv/doFv/MsM/xnf3Yvzc1tvPTSowwMtOLzlVFeniQnp5ElS84HCucCk97e
3rFQdV/fjy85J+IyuPgAyvld9XI4eLAbTYsRDvdRUDATv9/N8HCAnp49+P0pBgeriMWGOXz4SQKB
ALfddjfxeK/VevZqpk6dyuHDx6msLOPs2V5M04XTOZ9otArxQrqQRT5b0dHPOECYjICBo0g7EicS
EgkjnfGKEfbiN4ghOYEwEMsQo7MPCZ2EEG9ku7WfH2FKRhAwsR/xWpqs41OMez8FSIzXwM0xluOg
jk3U8RumM0Qald1U8o/cRD0eGjiMosywhpydRsDSX6MoM7DZWjCMx0inM2iaHa93AYHAVlQ1hWnG
Mc2pZDIpoBabrQancz6ZzEZefHGIsrLx2PeFjMz+/e3s3r2dgoLdrFw5d6zp0GW5LG8nF2oDPTBw
jJ6e57j99teHNNKI3pwrI6iqxsc+diu1tbXngdrPfe5LvPDCCF5vHV5vMYHAMG1tz6GqHbhcC7Db
byMeLyYQ6Ka9/VdEo2nKy6cA+1CUFZjmNGSxTyH6nocAgm4k3JFCgMMhxjvsJhCmQgOeRfQ4xjjb
mW2kd5N1zn9HbMAUQGcKo6zmEKvZw0JGiWJjI6X8A3/BC3yMFOsQZjPb+tuJsCZBkskt6Hqcb37z
b/jsZ+9+2+/e4/HwwAM/4KGHHmXXrpNkMs0UFbnGctre7PcqKipi7ty5l6wTcRlcfMDk9aWkgUAT
LtdECgtzGBl5npGRXFyuaiKRZjTtVQzDicfzRWpqSunoeJDu7qfYuXMvCxdOG0PRWbDidK4hk5lp
teR+BQEEowhzMRuJh0aQkMYxJAPbQIBBHGEmEoh3MoIAkGwN9VqEwhy2Hs9Z+yUR43MnUppmQwzR
biSx6xCSIZ6HVI60I7HcBGK4RqllH3Vsp45tfIQQHjJ04qQeP99mHtvIIcoUxg2dzfK4RjGMIuz2
z+J2X4+uq9jtk0gkOkmn9xCP+6isXEU4/Bzp9DZstslWaZ0Tuz2FotiBKvz+MoqLl7BnzyFWrRIG
5lxj8uyzG3nooRPnxcAbGl5F09J8+cvnRQYvy2V5UxmvEntyrIlbfn4Rhw65ePTRx1i9+i5qa2uZ
NMlFZ+ezmKaKqlaSTncyMvI01dXqebkVvb29PPDAj9iw4QSJhJ9A4BEghWHkIDqtoOtlOJ0pTLOF
WGyEdNoDhBgY2IVhqOj6IGIfsq2IrkLshh1JwpyNVIE9wbhjsQBhNfKQqrAkotenEUemD9gGfBXR
/TbAThVNfJo21nCIRTQRR2UTLr5LLZu5mSTlCNsRYby7ZxqxUW4ggKKkyc1diNfbzYoVS9/VDKZ7
7150LrgAACAASURBVP0ad9/97oHCB6351fsll8HFB0TeqpTU6YT8/MVo2mZisV8RiThIp1uw27so
L//PsYFgNTX/QG/vTygtPcK3vrV2jJrftu0YLtcN9PYm0fUKMpkyTLMDUXI/ovg/RgxCGlmgG63t
xYgym4hhyXbWm4t4LkUII3ECqeKYgzAQexHG4A6Erfg0kl8RQYzVFKRpjsd6rERCJzbcHGMFj1OH
Sh1tTGOYNCqvUMM/cA+byeE0P0HoVTcSv70FSfbcC3Tj9wfx+3MZGXHgdk/F4XASiaRIJNoxDD+Q
IpFoYng4Tl5enPz8dpLJYhKJGKFQO7p+BI+nhPx8jYKCXEpLr6Cvbx8///kjNDdHxkoF588v59e/
3k4wWPeGGPivfvUid975iUvS8FyWdy9ZNiwa/THd3QozZ36c8vKZb6gaWb36o3zve0/Q0nIUTcvB
MJI4HP1UV5eyfv1GFAVee62D48dP0tZmIxJZivSXMZD8heMICJhAJlNBJjOMNLUKIUDBjaYdRUD+
WcQhSCHs4UEk/DEbsQNhxDZUIXZgHjIq6ijCUExmPOdiMtKBdyliX7YwgSv4ND9lNZ1cx2ES2NjM
FH7AdWyimzgfQXIzUkjVyVbrcRJhOachAEUFWnA6b0BVPYyMNNDe3j42E+WdyqUKFN6LXAYXf2Dy
ZhTam5WSwk4qK6vZt+9hNG06Hs9sdL0dVQ3g8dSSm7tg7BzRaBsulwdVzQcEsPz854+wZ89pVNWk
t7efdLoa0zyDGILbETpxFAEHlQjDsB0pKZ2FJFSGGDdKo0iY4lqEddiKGJ+ziPG5xdrHgwCXXOv1
bNvvEsTjqERAxkxgiKkMUkczdZxhBe14aKMDN/Xk8lfM5WWWEOU269z/D2FRsmDlboS1OGR9E9cT
i72Az6fhdufhdLYxOqqSTMYwjB6gDZuth7y8q1CUKDfeOI9bbvkoDz+8mcbG7Xg8dny+KykuXoSm
7aa6eibpdITBwbPs3DmPqqrxUsGnnnqMs2fbmTDhjTHw7u6NtLS0XDZWl+UdSyAQ4NixfmprV1+w
amTlym52736VaDRNOm0jkwnjcKj4/ROx2+fz4x9vJZXyUll5EyMjozgcyxAnohRFuRbTXICEIFSk
LLwAYSndiCNRhuRTGEhVyFlElysR5uFZJBl7IsJmGIhOOpAwqIaAEhMpFDStc9sRfU9Qwat8EljD
0yxlmBQq9VTyGf6F5yggSol1fT9ivBrlDNLt4CaE+cwFdiIMabH17eWh618imdRwODa/obPrud/x
pRjGeL/looMLRVHuRbJzypG79BumaR54i/1XIHf3HCR777umaT56sa/z9y1v1SAnHo+fV4Y2OHiQ
s2eD2O3zaW/fiddromlteL0ZXK5RIIKuQzzeRzB4mLy8BfT0/JRQ6Agul4JpRti6dRtOp4udO2M4
nXcwMjKDZLIf03wVWdy/hIQ2Eohy1iI5Ff8biY0WI0ZhD+Id/APiLWxEDE0jYmC81iOMeC0zkO54
YcTwDCEGpwVhO5KADQ8trKCHOqCO15jKr0nh5BVm8PdMop6FnGYB4imNIgDnCYRZSSCJpNmpqmVI
7DVsfY5yTPMkfr+dqVMDnDr1OJp2FaZZhqIkgHYUxY7Xm0NNzUeAV5k1axoPPvjXbN68lY0b99LZ
eYhMpoeamnmUlEyjs/NpwEVV1R3nGf2BgQGSyZ1kMu3W95SVEetax+WyUbssbyfBYJBAIEVRUQ7x
eHxsOm9eXjVtbRnuu+9+XnopRSbzJ2jaRBRlFNM8gKal6O5uZnCwh1TqRtra+kilBhF2Lw+owDRt
jIcrliK9Zp5D9PMm6/ldyADAEHIPHwbWI4u9HwEOUxEbUILoogOxHdLMTh4NyHJQDfgoxeSTHGAN
x7iBATKobKWAz3E1G5nMKMXWe85DwiovILZjLtKA6xngVwjI8CDAJoqAo1pE10bJZLaj6/Px+10U
FBSc991eyAbPn1/OsmVLqKysHKvGuayj70wuKrhQFGUNAhT+hPEmWi8oijL9QvNCFEWZjNzBP0Lm
Y98E/ExRlF5TWit+aOWtGuRcf/1iolGoqKjk6NHj9PWNkkrFCYWGMYw9uN1Ramu/zOLFt2G3a3g8
hYRC7bzyyjcZHf0J3d1DJJM2bLZJKIoJlPDccz2EQocoKbmX0lI/3d39mGY5orzHkHyJYkQpfcit
0o10x1zBeC7GLxHKsxFRZg9iaExkMbchip5CDM9WhEHIWOc9ZO37DNM4SR0nqWMfKziDG4N2Bqmn
mr/gfl7mdmK8BHzbOn4AmWHiRoxYHwJoqhGDE0Juu2OIN+W2rmUQRXHgdF5DUVEzNTUt9Pc3EAw2
4nDkkZt7FT7f57HZnsdu72L//ib++Z+fpKIihyVLpvHoo//KM89soKFhgEymB0XpYdmyPA4dmjI2
SC4rkyZdgdvtY2TkGVyusrGR7OHws1RVuamtrX3XnRcvy6UpiUSCrVu30dBwknR6Ix5PEdXVVVx5
5XWEwx10d5+htTWMrt+MaS5GUeyYpo1Mpp1QaAOhUBxQUVVpRqfrDcgC7UYYShuST5VBWIVSBOz3
IfZAR5yDPISxKAf+FHgIYTYXWMeWIuGNlYhj0YE4ATMQn/FhIE0RndzFMGvoYwV9GCi8RC1f4nZ+
wyAjRJFZQyWIQ7MPAehtSLVJN+KozEPyM3qs6+q3Xrse6YGx0Nr2OHAQn68Uv99Be3v7eSDhXBtc
UVHKkSMPs3XrFn75y33Mnj0Rmy2ErueTTDou6+g7kIvNXNwP/MQ0zV8AKIryNeBjSEOs719g/68D
raZpftt6flZRlKXWeT604OLtGuRcf/1i/H7Yv/9F+vrKyMmZzqRJhbS2biYYTBOLxUkmDxAI9DJ3
7ieYN28yRUVTmTdvOZHISXbt8uJ0/hEu1yx8vgCZzD4OHz5DKDSA292KzZZLMhnCNINIIuUgEvrI
QdiFqxCgkAt8CvEEXrWuvhLxYAqREImBxDpzEUChIABiAMnRaEW8CwceevkI/dSRoY4RasmQQmEX
efwtc6hnEWeIIiDnSsSAPYLkY6xEvKsQEg/usd7jWiSe24uEWgaQ5LA7reMGgX3oepr29hJ6etZT
WuqisvJmIpEApjmBdLoMp9NOONzE8HAYr/c6Kipux2bTx7L1v/Odv3xDe+WWlgffUCqYTg8xc2Yp
4fAg8fhPicdzgAgFBcOsXfsxioqKrI6Ab9958bJc2rJu3Xo2bepE0wyGhupRlCl0d2+ntfUZJk/O
RdMi2GwTMAwfArZfwTQbMU0NAfwTgWsxjFYM42Vk0d6DAAk3QhTvQgDBSQRQuBCdyY6K6rb2HULA
RQDR+UXIIv484oB0AE8huRt9iN7fQQGN3MkgqwmykiYUTF6mkK9SxrPMJsgqJHz6I+s6yhifM7QT
YUlGrPettq5jJtJcKx9xcn6JgJEvIrbKQFFmYpofAw5is71ENKrxwANbqKjYMzYR+lwbfPToY/T1
qXi93ySZjNHYGKG19UVmzpzI4sV/ellH34FcNHChKIoDWZX+d3abaZqmoigvIbzaheRaBJKeKy8A
P7woF/kHIm/XICeZTJJMdnHs2FEU5Y+IRovR9cNEo3tQ1UXACIqyinD4JIcOPY/N5qaiAtxujUSi
HK93OqY5H8NIkEjYCAYrSSZPAfk4neUYxjwymQNIdYaOZHnPQpR7N8I2xBCPJZscZSBeTQLJa5iG
sAifRXIetiJMhgEsQYyPnelo1BGljkGWcxI3GdpwU08B9ehsZyYxShBW45R17lzgOwhbEkU6fPoQ
EOFFPJd9CMsyjACdEwgjkmtd93PWMXmIURwklYqQSiWIRhPYbBvw+6/FMOaQyfjo61tPOt2A0+nC
Zhvg0KGnKCsrx++vZdu211i16tY3JHe9vlQw26To85+/2ep5cYxQKEJBgYeVK1exevVd76rz4mW5
dKW7u5uHH36WxkaNSMSLaboxDA+qOp2enh1Mm2Yjk7ERjfaQyQQxjIcR834LkuuwG8mJaEcW7+MI
+N7PuI57EKAxFwEXZQh4z+q43dovW4WRYNzJiCNhkULrfCsRlmIPeYxwB05W8x98lBZswA4Wch+f
ZT1XMDQ2WOxGJHdrL6LnSxBGpZZxNmUh4vS8ggAMp3VsBLE/K6zP22h9nnxgxEpQj6AoaaCQwsJP
UFOzaqyT8cDAk2M2ODtPxOe7C7d7OoHAK2ianfz8zxEO78QwMmO6ellH31wuJnNRjPBsA6/bPsB4
28XXS/mb7J+rKIrLNM3U+3uJv38JBAKEQiHs9vibNsjZtWsPPT05eL29mOYh0umDRKO92GzTyM//
LInEg0Aau30ZqdRGTp3ajqaFWbasjKee6iGV8mGaWzHNEJqWJp0OAv34fG4M4zipVCGi1CcQYFGJ
gIwYYiz2IN7HQkRpJyAeTYm1PYTgxWKEfjQRQ7EBLzY+Qi911FNHPzXESWFjJ9P4G66mnhLO4kA8
mxEEOPgR49WCGMKliOE4gRieEuRWkWZfcmzcerQgXs4pxACBsBbZaanzEM/rf5HJ7EBV3TidnyST
MUmnB/F4XkDXZ5NOr0fXa8nP/wITJsxjcPAXtLRswev14/GE+fnPH+Eb3/jT8yjRc9sGn9ukKEud
rlp16xvitd3d3e+o8+JlubTl8cefpLHRTTJ5M6p6DZoWIZPZgtMZw+2+ge7uegKBCtzuCcTjnZhm
AtNchYDpPhSlFtMsRkaTFyLMQgjJTcogjEMHwjT2W/u4EfA+AdGxUQTQb0d0qcR6fSHCIOwk2wI8
h1/xCVpYQxe3kMCOyW5y+HOu4Bn+kQFMBBzkIjkdowiYWYQAliSi793WPvuta7oV0eWHEYfmY4gD
kwUcT1mfOWwd40WWkCDQjKKkUNVCpk2bT0FBBWJX4OTJx9H1GB0du/D5ykinRQeTyTCqqmEYTvLy
ZhOL7SSRCOL1Fr0vOvphzuH40FSL3H///W/I/r3QeNk/BAkEzu/eFo1Cb28Pkcj3WLjwfoqKZox5
vStXlnPsWD9VVXcxMvIyun4jhuGmtfUQ6XQlmnYcpzNDbq6fWCxGKtVGMnmU5ctXUVd3Mw8/vAOb
7QixWC52+ydR1UkIWOjHMCCRSJFK/TOihOXAckTJuxBwoSAeQCES7tiCNMBKWp8m20DrVwjzkWYG
bupop46zLCeOi0O0kkM9k6mnjO1MJ04T4iGtQoDKDqRT5wnE6zlubV9o/R1AjIZhve9MBET0I1Tp
KAJo5liv77GuMY0kdV1h7dOPGNFmYCaGUY2ilOF227DZvGja85SUNGGzFRGLXUt+/mzC4R1EIioO
xzdJpYbx+4Ps3DlwXtMseGPb4NcbjAuVsb2+82I8HiCRCBKN9l30GQRPPPEETzzxxHnbwuHwm+z9
hykfJL1/rxIIBDh5cginczGhUCGmWYLDMQtV9aNpD2MYhXR2ppg69WYCAT/x+DNEowFk0T6DwzHB
6t+SzZ1KIH7fXYgehRHAkIvos4LofjlSMWYgwP03iHNxI8IERpD8io1AHB86H6eP1cSoYxQ3JnvI
41ss42nm0ctZJHx5HGFGZyKhjQPI4v8kAi4qEBI7jLASP0LyOWoQ/T2FAKJlSL5XM8JQLEHAU7YZ
11YkpDMZVVWx2bpQ1Tk4naUIi7MYAK+3kiNH+jCMIL29v8TrLSCRGEDT9qIofqZMKWVgIDo2bNDj
EZ18fXfUdyO/rzyr36XOX0xwkQ3Slb1uexlyh1xI+t9k/9G3Yy1++MMfjg2P+UOU1wOK48fb6e8f
oabmGq688h58vh4OH37IGn98xZjXO2XKJLZsaaCmZhKTJk3j9OldJBIGmtaIpgUZGQnidLqx2/Nx
uVx4vTnMn1/MihU3kEgk8PlA13txuW5F1/PR9S5k0Z1LIrEX8fR1ZBE/gyhmdgE8jdwiTqQm/RRS
anYAWfDzgcl4Oc6NnKaODupoYQoDJFHZiY3vMJV6vkQjH0fyIDZa72EilO1UZLEvQZR9n/U+IFnl
N1j7dlnH+xCQ02/9P4QYPAfCcpRb55zOuDHcgoCmiYiRPMl4DNpHOm2Sl+eluvoaotEm5s+/noMH
t6KqKpHIK8Rix7Hb7waqSaW2UVU1l6qq696UEn03tfDZzovr12/k7NnnCQQixOMxNK2Dj350wlg1
wMWQCy3Chw8f5qqrrrpo7/l+yx+63r9XOdej7e3tpbGxn1RqGslkF4qyB9OchWmqZDJhTDNOOKwR
CjWQTsdQFAeqGsU0+1EUN3Z7DEWJYrdHyWSCyKIbREDDM0jScxHCGlYjzsRGhLnIttU3EXbAg+Qw
LQDuxEsxt/Esa1jPx+jHg8l+cvhbruJpPHTxTQQUnLLO/xgCGBYgNuQ0kpM1A9FlJ8Kc+hAdXWBd
74j1ehtSATYRuBKbLYSiJHA4hkkkQgjQKEBVv4xh1AObsNlqmThxAqWltUQiM1CUXHp7dzJrVgCv
t4jDh3fQ3x/mhhv+nJISN62tZ4jFnieR+Ffmzr2PKVOuIRA4RTC4jdmzZ74vwwbf6YTb91t+lzp/
0cCFaZqaNWp9JXKnoiiKYj1/4E0O24vw8ufKzdb2D6Sci1APHz5Ef38OEybcSiKxEK83h76+18jN
3caCBWux2x3EYo9z3323UVlZybZtO/nZzzZz6lQvzc3/wdSpC/F4uhgYSGEYU5BQhA/DaCYS0THN
M3i9hxkZuYr//M/N2O1JdH0UVfWhaUHS6X0IRgsyPllwAVJNkX2+GwENFQhbcAzx+H1IolYXMIWZ
HKWOQepoZxm9uOikBTvPk089s9mOkwQ60iTrOiTW60MAxDPWt+NGaM8exGO6A6FEjyDAI9uxb651
bBsSevEiNK7CeJvjaYzX5fcimFRHQMd+BETlWdv6gTSK4gHqMM0GFGWUZLIdt1uls3Mfg4Mn8Ho1
MpmzJBLduN2fQlE6KCy0MW/eFTid5vsWtli9+i527/4rjh+PYbffgM9XRkFBkoGBRtatu5ww9mGR
LGDIyoWo8At5tIlEFz09w+j6WVR1CMM4RTq9Dan8SOF0ukgkRujoCFJS8mkmT57FwMDPCAYPoao1
uN0KkchpdP0IinIW09SRxfk4soBPRZrYuZAwp4Ho6QkkOdKFJHLnAw/h5hXqKGc1T/BxtuIjwUGq
+UdKWIeHDu5mvJrkaoSBcCLg5GbgX5FUOgNhUWYg4Y7/QsDHRMZ73nRa/59FGFINCZMWA22Ypo7L
pTJp0kI6OjaTSsWx2cowzV3WZ7Gh69MYHCxF02qw2xMkkyn8/gAjIx0MDjbT3r5pbLhYbS3MmXMl
7e01dHX9N+n0r3nhhccxjBT5+WE0bZTW1ij5+Y73PCfkUsmzuthhkf8AHrFARrYU1Yuk/KMoyveA
StM0v2Dt/2PgXkVR/g9S37QSuatvu8jXedFk3br1rF/fRjCo09qqk8ksJRwGuz3CzJk3oWlFdHWt
Z/r0AE5nCd3d0vtg27adFrL9DDNnRjh1qonjx4+i60FcrpXEYjYcjgLAhmFUoGm7cblS6PpMSku/
TEXFXA4d2kZT0z7i8RYkZjoVm+0qZNFOIcrtRRbpLHsRRxbuEeuYCkDHh8GNKFYy5hYmEyWJwg4m
8G0KqSeHJmoRAzQFYR22InHQEcTj0a2/UWSxr0c6+fms6+hBjMdEhB7NIGDDiRigYcQgfg4BIqcR
oNDGOPAIIaGQA4z3wAgiFK7Puq5rEE8shM3WgN0+SlWVh1DoUaCBYHA6lZV3YxjTsdkUIpFfYbM9
Q17ebcyZM43c3Nz3dXRyPB5HUUpYvvzz5ORMxePx4PV6GRg4/qEyNpeqZAHDzp2nOXWqm5GRAPn5
LmbPnsHy5bPPo8Jf79EODBzjlVf+g0xGJx4fxm6/E02rwDQbgPUYxiESCQeG4SWdrqW310YoNAis
QNebsNu3UVi4mHT6MLHYKNIdcyei1ycRPepAwp4OZEloQkBHANGlz+HEyS08xxpe4BO0ksMxjjKb
f+E+nuJGWigA/hYB+IWIrhkIc1iLhGFMhLXMRfS7GGFLSxAHoBnR1z9BbMhWIIWqfgrDyEMckQZE
r52oahC4BkWx0dv7NKnUbkzTQyYTRUDL5xFAcgWZTBnhsEpRURm6/iLx+FF6e3+BYUQpKgpx5ZX3
EI/HSSQSeDweamoW0tnpw+Hws2jRrZSWXkE6HaGz8zdcfbWPL33pj9+zTr7TCbcfdLmo4MI0zXWK
ohQD/4S4kkeBW0zTHLJ2KUdSgLP7tyuK8jGkOuTPkLvpS6Zpvr6C5AMhWYQaibjo7U0C08jN/SSJ
RIhIZB89PS1UVVUTChkcPvwqPT2DaFoj//7vv2RgIMi0aX9BWdk8Cgs1HI4cTpzopb9/Hw6HB6dz
Bnl5c8hkQsTjYJohFCUXTbuahoYEjY27aG09QCJRgSzKJwAvup5lC0aQuOcyxIAcReKns63nLzGL
GHXso45+buD/4MKgGRfPUUI9q9mBiwQO63zzkfwJAyGqAowbmOXW693A/zDOImRHJRchgKPPemBd
7zUIy/EUYrSyfTOeQrDq1SiKgQAOA1U10HXN2veItb+KxI07rfeVhVxRHPj9Z8lknsDnyzBr1pVk
MhqvvZaLw7EMn28qipLEND14PPOJxzcxffpMams//r6PTh43NjNxu8fzBz5sxuZSlSxgCIUWEAwu
xW53EQzuob3dxshIN1kq/EIerd9fgWEUE48nyc//KMGggab1IvqzEBi0Ft5iYDKmeZxEwoWqerHb
byQnJ82iRXUcPJiguXkfsoDnMF4JoiDsYDPCEPqRZWEUB718FIPV/Iw72EsecU5QwfeZxDq+QiM3
M97T5rh1viJE7/Ks93mZcWDxGqLzCuJ0TEOSRX2IHbgayZF4DvhjhO1cgGGA2KZZwI0oytOYpoqi
DKIoO0gm2zFNO6ZZjXTj7SWbWK4oZSjKaWy2CnQ9RjTahtfbh9sdx26Pk8l4iEQyPPfck8AUdF3B
73eTkzNMKDTM9dd/ierqZef9ns3N63+r++GdTrj9oMtFT+g0TfNHSEbOhV57w9QmU/isD07Q9y1E
uunFCQTS5OR8nHj8ZQxjAJ9vNslkEyMjjXg8/SQSg4yMtKAo7cyatRJVnUpz8y/x+ZJMmMDYiPTc
3Ajr1/+GoqICUqlS4vEgmYxJMplA17txOqvw+2tJpyfT0vIT0mkd01yLLNiHkaTJjQgjcKv18CGR
qMP4WM9KNlDHAHUMUU2GBA52MINvsYh6hmimAcGEX0WSwF6yzjMJYSVKrPP9PwQwLEIMQxphEK5E
jM9HGG8rHrWeBxBvKogYoTSSdPYIwojUIUlb+633fRyoxOnMw+udgK6/gKJkMIww6bSJoswgne7C
NJutQWVXo+sBVPU1IILLZWPyZB+f/vRiCgry2bBBwW4vpqjoDjIZiMWamDLFzZVX3sHx40eZMOEw
fX0d7/vo5EvF2FyKkgUMubl1dHQkyM2dhd9fRjRaRDi8nurqG9mz5+WxJOBzPVpN02hp6WN0NEQs
ZsNmm4bNZsPr9ZJIxDGMUWQxX46wgDsAH6YZRtedwGLC4SDHjnURDHoRNmAJkot0FtGzASSU+CqQ
j508buRl1rCbO+mggAynKeaHLGcdizjNncDfIblR5YyHV7Zb53MwnoytIUDiEev/duvvVGv/40j1
Vh4Cdm62zluPOCEJhLQOwFjLbxXTdAHz0fWNKEofphnD6bwPRfkIpmlD005jmhNR1ZMYxhxstiHg
BXS9GU3z4HAYRKPT8Xg+S2XlbA4e/EsGB7ehKAux22dgszVjs22nuDhCWdn8837P9wPwX2jCbTaB
//1yWP4Q5ENTLfKHKIWFhdjtCeJxlbKy+SSTXQwP16NpcbzeUmAHo6NHiEYbsNla8PvzGB724XB4
8PuLaW09w5w5V44l9WlaEK9XwW4/QiwGsVgFqprENE8BhWhaiGi0mUSimFQqiDAJRYgn/1EkOfI/
GR9v3MZsTlPHDurYwg0M4cSkCT8bKKGe29jB1STHxh9nm9eMIrHYxdZ2t3XO7JAimZwohqQAYU4G
GG94cwYBDuUIZboHqfJwW8c+bv3/HEKr9gC3oqolKEonuu5HckVexuNZiMezklTqecrLJzNvnp3F
i2vYuHEfx4+fIp2uxDSXYprC4CjKYUwziN3uw+uN8Cd/cie3376Kf/qnnzFhwscJBF4mkxkYG/Y2
MHCa0lKdhQun8a1vrR37Xd9PA3CpGJtLUbKAwe8vJZ3uGKtscburCYfBMGz09Y3S0tJCbW3teSCz
oeE0bW0qbncV8fhhNK2LVGoKHo8Nl2uIZDJg5U+kEQbgSsQvGwSeQtd/jKpqdHR0Y5o6qnorhtGA
VFjYrEcfNm5hBRtYzTe4iy6K0WjCx39zE0/Sw0nmIImeRQgDOA2p0DrJeOdbHbEHISRsUYkwhUkE
gBQhOnsLYkPOILbjOgT0ZKch11gPn7Vt1DpHGwJYepEE0EFgALs9jWFcg2Fcg8NhwzBsKEqlVYqb
QOzOUgyjG8M4i6bVMjjYiN0+n3DYSzDYQji8CGE6dwMjZDIRFCVKIpGmv/8MkydfM/Z7vl+A/63K
1j8schlcXEQpKipi2bI57N+/hWDwMAUFt5FKPUEo9DAul0ZBwSBTpqgcPlxDael95OUtJpnsoK2t
HpcrTTD4Cl1d06iunk843MHo6AFmzJiMaSqMjDyH0+lH18E0Tez2akwTMpkjaJqG/LSViLIXIgt9
AD8qK7FRxzrq+AlVJEmgsh03f0k59Wi0MA1Z+L/EeDJVHPF6zjLetW83Yqh0JKehDwEHnYjBy3bm
y446dyDgowChOCMIFXsMMSaViHF8FjEibus4L4oyEZerFK93JrFYgGRSB1R0vRG7PYPT6SSdjnPj
jUu5996vcdttJ7j99nvp7r4Jw6gFClGUldb7PYbfX0hxcS8337ySRCJheYzzmTSpi7NnZZG3L2XS
wAAAIABJREFU28sIBFro7W1j7dpZ73qC4ruRS8HYXIoiDkaS4eFmVFUhmQzj97uJx1uJRALs3XsQ
w2jkv/7raVaunM/ixdVs3lxPIpGgvX0IRfGRl1eEw2FjZORJTHMuyeREiosdBAJnSaXiSI7EHchC
34MA/RqgDV0vRtdPWl07hxGA/xFUXuYG5rCGrXySxyglQSs+fkop6/grjnIC0eF5iNOwGdFHP5L/
NBWxA6sQu6AhrGgzYgPaETCBdT2VSOjmVWsfFXFwRpCcj6xo1mMeAl6eRyq/aqzX+4GrUJQMitKJ
wzEDVc0nmewnnXahqg5MUwGarAGM5cBJdP04hjEFXS/ANFMUFc2nqSlGNNqOYeTh8fwVpvkwOTkf
RVGmo2nHyGT+kfb29Xg8nvcd8L9d2fqHQS6Di4ssX/ziFzh69AQvvfQomtZKXl4VEyZ4cDpPcMst
s2loGKawcBou1zzs9rwxjzkabaeqagCHYzOdnS/j98Pq1TPQtCmsW9dCXt4VlJcvJJEIMzDwIplM
NVBHOv03iGK7EIpxLnPwUcfz1LGRpbThxKQRG89SQD1T2UmS5NhiPgEBAGeQQWD3ICGPboRFGEVC
HSVISZodidnWIkDmGBJbPYuEXw4jrMR0hKE4hsRiY4xTpSaStGkgACQHARmnkHbE+ZjmKRSlCLvd
BwRxOp2AHZcrRW5uCq/XhdudZNmyJYAk0SlKCVVVK+no6MIwpqCqlZimDUXJxe9fSDTaBZwflpgz
Rxb5rq71BAIhbLYWbr991UVf5C8FY3OpSSKRYNOmLXR2NtPS0o+uz0HX5bcNhV4gk0mTmzvArFm3
4/Ndw4YN9dTVlXL77RPZvPnXhEId5OXV4HYncLsXoetn0PXn0DQVl2s2kyYV0NzsRYB4ERKCyLKS
c4BmDMOD6FACBSdLgNVs4VO8SAUJOijhUT7FkyzgENOBXyOL/0Ek8TI7F8iPAIIBxFkZBNYgCaJF
CLuwBGEY7Ag4uBlxIrqQkVHZ5M5saCRrZyqt/WXGkORf5KAoaWy2ILr+stVhExRlMqZ5M6Z5Bofj
FAUFPhIJSCR2oOu34HDI585k9mOaR3E4HNhsKTRtCLf7OtzuNtLpDHl5hRhGOQMDbUioZQhV9eJ0
LkRR8kil2vH5Kli+3E9f38UD/B/mEe6XwcVFFo/HwwMP/ICHHnqUXbtOksk0U1TkYsmSq1i4cB7H
jj1DTc1MWlubAHC789B1D7HYMPfcs4Ivf/mPzytf83g8RCJRvv/9dQwPH8Ru92CaGTTtauz2EIoy
Bb8ZYyU91PFj6ggxiRBxHGwnn7+ginoStHIT0p3vMJIgeQ0SOpmPGJFnrNc8iAEJIHkQJmIIgkhS
loIAj+OIZ+JEmIlPIOCgEWmwpSJeRw4yTCjbzGs7YlyiCDtSb51jDmLQiq3HIPH4UTKZZiCGqjZQ
UHAVHs90rrnmauz2JA6Hi8rKynO+/TQOxygej4d02ofNBqYZQNd1TNNFfr4o9evDEjNnrqKg4Bg9
Pc9x++2ruPfer/02t8C7kg+zsbnUZN269axb10JJyVdxOBrp6mpgcHArwWAc08xQXLyQmTPnMGfO
XTgcUi1y4MB6vve9b3D99Yv5+79/gN5eD8PDJfh8ddTUVDM4+BJDQz+huLib3FwnbW1t6Hp2/LgN
YQlVxLkIo+DhGnTWEOXT/JIJaHSTwxNMZB1r2M9CRId9CNPYhuihibAcFciMjiJEl59D2AYXop+j
CAAJWscNIEAjG0rosa7nKiSHYg2iz/UIyIgjwGOI8ZytWSjKMuz2FGVl+USj+0gklpNK9aKqdlS1
Fa+3hNLSRVRU+Dh6tBGnsxJN+w2a9iSG0WG9bzEeT5q8vHLSaS8VFffgdFbT0/M/xGIv4PV+FEXR
UdVuNG0PPt8VKIqPRKKLTOYI1dV+/uzP/hTgMuB/D3IxZ4sUIIXL2RKCZ4BvmqYZe5P97cB3kay9
GoSLewn4a9M0+y50zAdFPB4P9977Ne6++3yvNBAI4PeDz+fG4XDQ1XWacBgymRZqa52sXbsGr9fL
pk1bzqt7N80hiosLsdt9+P0fp79vhKmJI9RpW7mVDpYyigM4i5NnyKee69jJbFKkEaOxG0mUakUM
igPpunc7ckvkWX9/itCYpxCGYRJCvT6LGKRRhCJ1ICGObD17GDE811rP9yMloIVICKUB8WaaEGBi
ILkgIAZoHmIkpwDt2O23kck0oCgH0PVBVHWYVCrNwEAFNtsB9u3bzowZs/n0p6ePKX9tbS2TJrlo
a9uCwzEDRalE05rIZJ7H6fRQVeVg+vRJY7HTC4Ul1q5dcDkscVnek8gskM0MDNyI3e7A6ZxDTc1c
5s0LEI1uQNcdzJz5bQoKpowdc26y4LRp01i2bA7/9m9b8Hq/ids9nWQyjM1Wxpw591Bc/Aqf+9xK
gsEOjhwZRvT1Y0gFSTOL+E9Wc4TVJKkiSR9unqKSJ7GzlzxMcpFS7uyY9ATCOKaBtYhOHkXYCA/C
NBQiDkI9wkoOIvahAnEG2hHnYToCQGYgTkkjAjA8SH+LWQj7+TICRPKQmSDzEDvyCKqq43J5ycub
QTp9AnDicOQya1YRubl5tLQ0YrfHmTBhBWfO7AVcOBxpdD2NquaTTueQTqvEYnlkMil0PYzdvpHy
8vspKbmBiooe2tsfx+U6g80WRdPcqOpsIpFNZDIt5Ofv57bbpIPnZcD/3uRiMhePIynAK5EV5hHg
J8hkqwuJFwnS/S/EDS5Amm1tINun9QMur79Jxz3ml6ioqKO6egaDg02MjvawevVtTJw48Q0TM/v7
z7Bz5/8wa8IVrPXEqGn8FtePtjGRJHFsbFeq+HNzFvVcTxvVyFf/KkJtXoUYADviMWy1rsSDVHR4
GE+iqkTilXGyjbMkB8OPeDfPIqBiMWIcMgjFGUIMUCMSS81met9ovXcC+Azj4503IGBDQ7wjmRo6
njjaTibzEIqyFEVZiWk+jaYlUdVrMM1CdH2Ejo5WysuDrF791+c1Krrppqt56qnX0LRG0uktOBz5
eL15TJu2mNLSTpYvnzX2e1wOS1yW91Mee+xJmps1SkqW4fNNIpkM09bWRE1NKR5PBXZ7lHB4kFgs
g6IkKCiYQCTSM5YsGAgEqK6eSHGxj0wmRji8D7tdx+GIMjhoo6OjB5drBzNnFtPQMEQ6fSVX0soa
fs1qXmMKQwzg5GmWso6Ps5sSDB5CWIN5iJOwA/H5NMROBIGvIECiFdHbpYi+Z33CAiR8WojoqAcJ
pR5B+mcUI3lNjdZ+pxCHZiHjzfD2IszCIGI3PoWitGKaE1AUP+DCNJ+jqGgJdnsBMEg6/TCVlUu5
4opr0LQhQqED5OQMkEptp6DATl7eNUQiLlR1Ol1d/45hTMVmW4ZhVJBMtgMv0Nv7DPF4H4sXf4Hq
6qtRlHbWrl2J1+tjw4addHRsQtMUPJ4RKiomc+xYlL/5mwcvj1Z/j3JRwIWiKDORtOCrTNM8Ym37
BvC8oih/ZZrmG9p/m6Y5ah1z7nnuA/YrijLRNM3ui3Gtv28512MeGoKcHFi6tJyFC+fR1NQ0Xvde
OpeywRNc17iZr/fvZWF7Mw4MWhx5/MZWzGZzIru4lrSaRtMmW2f3ItiuAumKF0LiqD6knOxaJBSy
HfEgQgjIsCPGogNhNoqs/YIIfZlty7sLCWfMQ4xPCsmpKLD+r0GywQNIP40KJOnrGGLAsrMJdMRA
1SJ0627EaypEeqgVAXuw2TJomiSZORyfx+OZh90+QCLxGE1N23nwwR9x5kyQU6fOMjKSIjc3n9xc
F15vmFgsTiIxSlFRBbNmNbF8+awLshKXvZTL8ttKIBCgoWGAnJwybLYEdrsbv98NQGvrJhYu1DCM
UTZt+g7pdDk2Ww5ud4ry8hRf+cqNY0xlIBAnGh2luDjCrFlX8tprB+nsTGAYQex2jd6ePKYnh/kP
T4BbMz+g1hhiCB/PMId1TGEnt2BwB6J3g4iOXW09Hwb+CGEPf4qwDbORkCWIg5BEdN60jpfGc+J0
rEByul5GnIZRxMnIlm6OIvbhFMJaHmM812IJ8DTinEzGZluIabZgmr/GNGOoagRFOUh+vsbkyUNM
nmxjaCjA8PBWtm3biceT5oYbqvn2t78HwNat29iwoZNgcAouV5hkchRFWYHTOZ102oaul6GqeRjG
aXS9k1DoQaqq5rN69Ywx0PD5z3+GlpYWnn/+BQ4eNKmqumMsifPyaPX3JheLubgOCGWBhSUvIXfn
NYi7+k4k3zpm5O12/F3IxZhgd67HfO7skT17nsGZ6KWioYk7XM3M6thBbqSHtMPLXvdsvmNOY6ut
ml7XatJpg3g8iGkeBf0MYhAKkQU/O+inBDEIlYwnV9oQRW9EwER2PkcamcfRgTAJJQgocTHOaFQh
BNNR6xgnYrgaESMVJ5v1bbMdxjRVVHUuun7MKp0tAzIoShhFWY5hJBGD5LHO/SICNtYCCUwzy3LE
cDrXUlS0DIfDD0xEVTVCoW08/XQzfn8VweAC7PYljIykmDAhSm7uKe6808edd34CePtS0g/zpMLL
cvElGAySyXipqZlGa6vk8bjd1eh6J9HoK2hahqamNIpSg8NxLYZRSDTaQih0lAMHDhMO11BWdhfT
plUTCv2IM2deZHBwkIGBYlS1gLnKHtYYSVa99mNqtAAjqoODk1byi8rbOZgzl5NnjtLZ+QICytOI
HYgji38hAhp0JGmzE9FvG5IY2o7YhFqkB816pAzVQIDIbqS0VEPCGyFkKGA2HFKKmPpO6/grkBBs
lXUNuxGGMwEkrATNTRjGImAGDkc/LleUnJw4JSWzmD/fD+Rw8GAF06evwOHwo2lRAoG9vPrqa3zh
C2uZOHEi8CgPPvgs4bAP0HC5CjEMB3Z7Pg4HuFwTMIxSliz5BH7/cb71rbXnVX9l9byvT6eq6sPd
lvt3JRcLXJQjUHdMTNPUFUUJWq+9rSiK4kLc7cdN04y+/5f4zuWdTLB7Pxak+s0v0LmplTrNwfze
g1R178du6nR4J9AwbzVNU+vorL6BR5/8CW1tv8Dnuocc7yoM4wSm+SICKooRAugjiBL/G2Jgvorg
ujBCV5qI8h9HvIljSOTKRKjKAPITzkAMSRuSDpNvPY9a/4etfbP9K+LITyyD0Pz+6ahqgmRyNy7X
1aTTNaRSO4CfIYDEYY2CnsT4rINcxHDNITvrQFV9uFwuMpkUDkelBSxE0mkbhuElP38BgUAfubl3
4ffPIxodYHT0NNXVt9DcXP+2v83va1LhZflwSbb6yOebj8PRRFfXesJh0PUAVVVBdH0CyaSd6uqv
4HJNRdMSpNOLiMcL2L17PUuXrqWsTCbkzpixinj8UbQTP+XzmsqnjT5m6MOEFQ/PO6r5treWbQyi
jLopsNlwBPutrp+9iHPgQ/QphoQimhHgcBjR309a28uQss//y3iCZy6SI/ES48mbKuI75iG2Idvd
swYBLceRPhQRBLRcj7Cc2TL0BGJnpKGeaXZjmoPAVhyOAnJzZ+B0hliw4C6SySCPP76DTMaG2/1J
HI585syZhcPhYGAg/7wFP5t0/dRTJ9G0KLHYSTTNgaK4cbuTGMYB8vO9TJ26gqGhc0tfx+VSacv9
u5J3BS6sWSDfeYtdTGRV+K3ESu58yjrfn/625/tt5a0m2K1efddvtSAl+vrY/91/Rdmync+3N1Ku
p0ja3LTVrGRL3YM8FmxjX/8gy2esobx8Jv3dx4jF9uHx5OJy1RAO/4xMphPxIKKI4nsRgDAZYQLy
EG8jjLAP05BEShDDcAXi5UxnvJY9jsRdJyM/QwMSfy1EQMQO633CCMuwFyGYMoiRkkY4mhbGZrsa
n2+AcPhfMAzNeg8F8GOaTgSsZKesZpCMcxVhSTK4XEkcjhAlJQper0Yk0kos1obLVUIqNUQyuR2P
x6CiYhp9fX3k5YlxcLvzCIfB6SwlGn174/D7mlR4WT5cMp5Ltd3KpbqewcGTjI4eYPnyybzySjuK
koPbXY3d7sXh8OJ0+ohEikkm7SiKnaNHH0M/s4MVg0f4RrSJ2dooEcXFVs8K/t6YwGatBM28CTP9
LA5HAo9iR9MOYZp2EokDiO5OQdjECQjr0InoVhCxF6sQxqEAAQoK8N9IcrUNsQ1xxC5MsJ5fZ51n
ERIiLUZ0v4XxwWKTEACTsc7bZx1fyvhk4iIUxYNpDuFyJclkIuTlVVBZ6WfKlCXoeprubp10ejl2
exC3exlnzw4Ap1mwYN4FF/wvfvEL+P3r+fnPuzlxYjOpVC8223Rsthgu11Hmzr2JdDrypk2wLnfK
fX/l3TIXPwAefpt9WhEuvvTcjYqi2BhPN35TOQdYTAJufKesxf333z/W/S4rFxov+27l7SbYRaOP
sm1b+J0vSKYJx45BfT3U1+Pas4cVhkF37iS25M1nX8HXedVWRc2sYhYsmEfh0Gl8O++jp+e/iUQm
YLcnqayMEovNIRT6BeDF612DYURJpx9FlDqbxR1GAICJxFgnIAYkwXjzmqmIgYgjeRFTyOY4yM/V
jrT3fhwpKc1FPB0H8hO9ZJ1jkfVXR/pfvIqixDGMEIpiJxo9jWEU4nAswu1eSCIxhK6/htwOL2Ka
I6jqLAyjEQErGaAbRXGTk9NNWVkrX//6J1EUhe9/fwcjIylSqTJUdYDi4iNUVZWhqnacTkgmO/D7
55FMhnE6IZ0efFvjcKlMKjxXnnjiCZ544onztoXD4d/T1bw3uVh6n5X3ykheKJfq1ltnsHLlck6e
fADTjIzdp4BVCTLMDMcoi7b9LUt6jzEvM0IUG5uUQv6OMnZ57mYkeQWGcRRYJapGAIfjTsrLFwNH
WLhwIps2uRkZSSCOxcsIUM8u+scR/SpAnJEiZMHvR3Ixyqxtg4iDcA9iyk2EBY0irMSjiB2JIblb
dyCl6klstkrgNLo+ijgMLsQh6USWhwjwd6hqGlU9SnHxV62uuC0sW/YVPJ5Ctm17ELt9OR7PKHAA
my2BzzeNrq7TTJ8eJxJ544KfDTGvXLmcxx9/kqef3k1n52FycyuYNu1qysvnvGUTrEuhU+7vUuff
FbgwTTOAcOBvKYqi7AXyFUW58py8i5XIyrb/LY7LAosa4COmaYbe6bX98Ic/ZOHChe9093csb0WV
NTWl2LWrgbKyr7z1gjQyAi++KIBiyxbo6wOfj/QNN7DuujpOT74PrXIR27Y9iKIsRM3k0dCwk/7+
Z2lrO0MioTM62kN5+QC33no93d0KTU2HiURUYAqp1Cvo+nQUBVTVg66DqvoxjCHEqKhIclWZ9TiI
9KjoQoxPtk79DoTCzE5MLUDo01es4zzIz59CaNP9CMi4GQEWtQiYsaOqP8DrjWCzPUI8HkLTepAh
RMOkUttxOIrIZCYBjShKCwJ0rsRut6HrJooSxTR/gM1mo6amgq985ROsXXs3AD6fn82bDzI01EZJ
iZfbbvsE6XSa+vq95OW56O7eSDweIJORnIvR0Za3NQ6XIiV6oUX48OHDXHXVB2e0z8XS+982RPZW
1UcrV86noWETweCv0fUUFekYN/f9D7entjMnPkQclc3qJL5rX8uLtnuImaMYxk/IxHcgocQoooOn
AAeJRCnt7SFcLo2WllHEAShAKj8qkEU9YP1NIot7BrELFUjYtAuxEWeRZWEqcA+qWozd7iedbkec
jaj1N4FUgPWgqgoQxTCmALsxjF2AgqI4gE2Y5koEsPQj4CYHVdUwzU0UFMyhvPwuBgdfIB4/zvDw
GXJyJjA6GkJRUkyfPgWIcvZsPW73jaRSUbq6DpJK7X1TnZ44cSLf/vZf8pnPrOGxx56koWGATKYH
Rel52yZYH/ZOub9Lnb8oORemaZ5RFOUF4KeKonwd0YgHgSfOrRRRFOUM8B3TNDdYwOIZZHVbBTgU
RSmzdg2apqldjGt9O3krqsxuT5LJeMZo+Kzk5VahHOvD/O534cAB2LsXdB1mz4bPfAbq6mDpUjo6
O9n8j4/9f/buPT6q+k78/+szZ+65TCZDMknIBQgBAggCghcsXmi9Yqm0Yqm2rl27ta1tl1+763Z3
e93t+utF3a3V2qvipVRs6aIo9YIV3KhgiQTlEkIIIRdym0kmk8x95vP94yQxhAQSzJABPs/HYx6Q
M+ec+UDmc877fC7vD8WFl2K3OigoKOFvf3uY7u44weB+amvdwDyysq4lK2sWHR3P8cQTL9PTk004
vLJvdU8XsdhfkfIgRqPAZqsmFHL2LWrkAzoRIhspAZ5GvyjtRb+IuNEvNJPRny7s6F0WO/hgbMUk
9PEbVej9rwXoTa0z0ZtJ3+jbZgD2I4QBkymKwWDmmmu+RUfHISorNxONXoTB8HWglHh8H4nEVjRN
f3JyOqcSCtkIBqcixEwslikYDLsQ4m8sX17C7373y+MuIvpF+7rjLtrBYBCzeSPbtu0jEKimq+tt
srNdTJ1aNOLMkNH+nlWT6PlnvLrIhpt9tHr1KkytLXh/9QRL9/+CBeEuwgaN5gsvZM91X2DFo3+l
tWc1BsONaFoO6RYDweAqYrH/RA8AJHpXRA56wN9OLGbBarXT1BQmGOxFCIl+ycxDDyCOoNfhBHpX
pwG9Pqf1/exHb+3sH/PkA9pIS5uMwdBKPP4K8XgeeldIC3pwUYTZPAdN+z/C4XVoWhSrtY1Jk8y0
t4eJRkHKd5CyBU2bTDTaiJTV6AO0/weTqYDJk3+I1erAZAqTlycxmd7A4wFNO0x+fg9z5pTTv5bJ
wYNPEIk0YTLN4LrrLjhlnS4sLOTee78xptYnNSV9/CQzz8Vn0JNovYr+jf4j8PUh+5ShDwgA/Q63
ou/vu/v+FOg16Sr0WnXGnaypbPnymVRVteDz1ZMliyg9/ArTD21h2sHNOAIdyP9Lg49+FB5+WA8o
iouPO/dwN7Rg8H3C4Rz0C8JqDIYCIhEfkYgdu/1K6uv/D1iM03k1nZ3NxOPTEcKGwfAsJtMFwC7M
5pewWq10d3eRkXE1oZCVYDCIlP3dIx70pswV6KlH9qE3fW7ig9wUJgyGY0iZ37c4kobeDlsOONA0
E0bjbMLhd4FGbLYbEaKOWKyXRKIFIfT1FLzeToSYicGwAE0rIZFwIeVM4nE/+uJntaSlXcS8eeXs
2rWVnp4NCOElK8vIddct5v777xv2xj70oj30ojD4/3g0F4fzoUlUGZ2xdJGNqdvk2DH44x+xPfMM
n6moQJrNdF18MbUf+xhZn/0sU6dMYefOnfBkFdbYZOz2PIxGO8FgB5HIZPTgPwN99kYveo6ZamAz
sdhcMjIuxGgMkUjsxWg0E4u9iJQJ9CDkAHq3BQhhQspr0C/Nj6BfZn3og7anoI/L6EIIA+HwW1it
JpzOTHp7I0SjlRgMYTQtQXr6fjStlGCwCCltaFoXTmec6677Lm+99SR+/0zC4ffo7e1ASj82m5VA
oAsh8ojH0xEija6uzQQCU0gkKrjjjmv59Kdvwev18vLLW9m6tRavdz8ORwn5+RcQjVazbNkU7rrr
78ZUH09nermakv7hJS24kFJ2MXLCrP59tEF/r0e/g6WcYZvKbirl1pml7HvtNWyvP87MzgYMMkGz
s5S/FszGtmop1/7H98BsHvG8g29ooVAXBw++TTxeiMWyuG8U9UVo2iTi8Rqam6sxGtsJBg0kEmlI
6UFKI/H4ETQtH03LQohOEokGXC4bs2Yt5PDh92lpqSIWuw4pr0GIDqR8C/3CdAN68+Yt6IsSHUMf
Df4i+tNMIQbDEuAqpPSTSExCyiyyskrIyyugoSGClGkYjXnE49uJRhOYzTPQNDPx+CFstvkcPRqk
u3sXUs4iLW0qoVAN4CORsKI/UUVJTy9GSklvbwUf//g08vKmc+GF81i8ePFpLRT2YS4K53qTqDI6
o+kis9vto+s2aW2FP/0JNmyA7dvBaIRrroF16xArV+J0OHAO+gw9s6ydzs7DxGIdGAx59PZ6+1Yz
7UWvN+noDwnPobckvIXJtAdNayAYbMJgqMZsvgW//230Fo409OChFoPhIkwmG0K8Qyx2FbFYPZq2
D4fDSVnZ1YTDUY4d6yWRCBMM6muERKPVxOONGAx+0tPTKCpK49Zbb+DZZw/T0eEgN/ci2tubSSTe
JB430dKyh6lT57NvXx2adgFTpjiorz9EMLgdm+0SEomriMWy0LR22tq2Y7X+lptvXsLnP38HNpsN
l8tFYWEh6enH18XBeSmU1KfWFhmF/qfimy6vJfz88zh37MD6rUehtZUF6ek0zJjJ07MvYGf2dMJu
B0uXlnHt6lUnDSz6rV69ikjkD/zmNz+koaGTWMyFxXIIIXzEYg1AHvG4Rjwex27PBEDKDMLhGGBC
02wkEv+HlO+gaZ1YLBdis13OrFkrKCho4OWXf0xLy28wGA4CDkymTKLROUg5BT0JzmSEuBwpDwK9
pKVJgsEONG05iUQuEMBsvpBYLEYsJonHY/h83SQSccJhH4mEA/gLicRhYrEi0tIKyMlxkZV1A93d
DUSjL2O1+sjOnoTXG6GzswohHEAtmZkGPvvZn+P3txIM/oFvf/sLSV159FRUk6gCo+siO2m3yY3X
wsaN8Mwz8PrrIITegvnb38InPgFO54if7XK5uPPO6/n+9/+C1ysIheYRjR5EiDeRcjZwF/rg623o
DwNTgBoyM/MJhQ4SCrlwOq8gEtmHps0GlmA0ahiNLdhs+7FaD9PV9Q4GQwxN20Z6upm0NAczZlxB
efkneO21R7DZLmbu3Nk0NW3lwIGNRCI5CFGO2ZxLOOyjoeFtKit3k5kZJhLZi5SNaFobWVkX4nSu
oqHhRZYtu4vu7qM0N/+ZnJzZwGEOH/aRmbkSKZ2AhtU6g2jUQF5ejO9+91vHBQ2qLp79VHAxWh0d
ZM+cqY+dmDsXPvc5uP56xNKlFJvN3ODxcMlpVAKbzYbZbMbhWExurhufz43RmEMw+CvMMlcHAAAg
AElEQVQSid8TjUaIx6OYTG3E402AhsGwnVhsAZCBpsURYgcGQxdZWfrS7XrXhJmSkiUsW/Y1Xn75
m5hMGpp2JeFwBl7vf9K/poimNWM2T8dguAn4NWazk/T0bPx+H+FwC/F4PpHIOwjxGna7nWDwffz+
YgyGXISIo2lhhLgOiyWHrKxOZs2ayeWXf41AIEBHRxN//euf6eo6QlPT7zEar8BoBIMhQFpaM0uX
rsFmyyUclvj91uT83k6DahI9v52qiww4odvEKQu5bH+Qhf/2XeTf34GQEq6+Gh59FG6+GSZNGvaz
hnar6N2XMHVqhGDweQKBTUjpw2S6EE37GPG4k0gkDylD6CuY5mK1luF2f5WGhieIROaQn5+Fz7eF
3t4ZSJmNEF24XBfhcFxKJPIUOTn7yc7Ox2DIICNDw24PYzL1cPToI0Qizcye/WnmzVvA9OnFtLcf
weO5lEhEAukYjUXE45ls2fJbnE7Jtdf+E2lpOdTWHqOuzoCUTkKhCC0t75KVZeCTn1zBNdcsp7Oz
kx/96M+4XNeQlaUPpQsGgxgM82hvbycYDI74u1B18eykgovRmjQJfv97uPRSKCo64e3TrQT9/bul
paux22HHjoOEQgnM5tuQ8mESiZ8BfqQ0EI/PRMoioBUhqpAyTjzei8HQgtkcwW4vAbIwm3sHngJy
c8twOCaTm+skGt1DU9O7mEwO4vFLMBjKMRr9RCIvYDCsQ9OsGI1zycnJwWDYS0fHPoQ4ghDd5OS4
MRi+zLFjbyPEG0hpRMosbLZ5WCwrCAT+htV6OZ2dbxMIeLDbXdTVVZFImCkvv4rGxv10dv6KWCxI
evpkliy5kXi8jK1bd9LdXYumvcfLL2+lsLBQNXsqE+5kXWSNjY309MCMXAfzd69j7t5nmHb4FUQi
zv7cEtq/8x1y774bcnNHPP9Is1Gi0QhbtrQxZ873WbAgg/ff30RFxUb0QdQGYrFaDIb8vlZFgdV6
iJyc6YTDRzAYNCZNuoREopr09OkYjVfQ0uInHu/E7/fj9wcJh3dTUlJMWdm/DBk/5mDx4oX8/Ocb
SUvLwGQyEYv5SU/PoadnKkIcwWye1LeAWgbBYA4tLV288MJ9LFp0I5MnLyESaaKubjuJxN8wmWJc
d938gW4Mj8eDy2VB0/zY7fpibXa7ndbWPWrA9DlKBRdjsXr1uJ9ycP9udradeDzOe+/V4PN1I0SY
WbMidHV1EYl8GiFm0ta2CSm/1Df7YycwiUSil2BwPV1d+4hG/48LL1yE3W4HIBJpp7jYjtVqo7PT
RShkxWy+gXhcYrW24XLl4fMZCYfLcTiuoaDgFmKxVtLS/hfYgc12JXoTZibR6DSEiGEwVCJlHCmv
Jxw2o2ldQJxgMIAQnXR11dPWdogjRzZTWnopy5Z9i0DAg9dby+7d62hr8+DzWWlr82I0WhDiGAUF
S9m61Ud6ukpYpUy8EZvlu7vJe/VV7q1Yz+zG/8KYiHG0+HJeuvZBtuXMptOynfu+8hU4xYPGcN0q
Gzb8kd7eWsrL7x1oEbFYFmI07iCRkBgM05GyBSnr0LRmoIH09EuZNesGiorcvPPOAQwGA6GQA4Mh
hpQdCJGBwWBDiBJisfeJxwVO57QTBqpWVW3k058uZfnyCwZabMzmDCKRdsLhv2E0FmOxTCMYrCcY
rMVoLAWW0dn5Ptu3/xWj8Wn0mWbdlJXlcfHF044bH6EGTJ9/VHAxwQb377rd81i0aAHl5TM5dKiC
RGIW//qvf8c///OP2bv3IKEQGAwOYrFi9Ix4JRgMC0kkjEhZRW9vNWlpL5OToyeQ6q+8t9/+UXbs
+Bvvvfc28bgNmy2LtLRsNC1CQUEEi2USvb2XYLcXEosxkNgnGq0mFtuB0VhGNGpB09qQciOJhBmD
YSpQRjxuoqfnGAZDGKu1DoPhEB7PHzAao7jdPSxYcCcAdrsLu92Fw1HMtm1foLn5MTStHJvNSVFR
GXPmrMLrrTlnE1YpZyeXy4XLYoHNm/UxFFu2kBEOkz+9jCfmXEvN/K/B5CUf3Civ1m+UJ5tFMtJs
lK6ueg4c2Mv8+TkABAIBWlsTuFwX4fXuRtMm43ReTCKxl2j0RTIzJ+Fw3ExHR4z58yczdWo5e/b8
GYullJwcN0eP/hGjcSGTJs3Ebg/Q01NNMDiH3l450LoYCHiIx2N4PAFqa2tZuHAePT1+qqr05F95
ecfwepsIhS7F5zMQidQA9VgsBRiNmUh5AfH4NMLhV7HZrsJuryYtzTHsg4IaMH1+SVpwIYRwok9F
XYE+FfVPwNellL0nPfCD4x8F/gH4Rynlz5JVzok2XETv99cDldx881KcTidZWUVYrXXE44eIRo8R
i72BPtPjIoSwkJHhRdMKycpaREFBBeHwsxw9ah2ovMuXX8HOnfUsW3Yde/a8hsmUR1bWxfT0tNLR
8QqBQACHo4CCglzq6moAMBrdaJoTq/UQWVnNtLbGgBys1hZCoS8hZTuJxF+AxUiZgcHQTW9vDddc
k8e3v/0FAH7yk6cJBNrIyPhgOZlAoI3S0ink5WkUFHyOrKwS7HbXwL/9XE1YpZylnnwSvvhFCAZh
yRL44Q/hllvIyMnBuGEj3ooKeo5WDNS1m266nnXrnj7pLJKRZqPk5s4FIrS11eB05hMMBolEICtr
CbHYNnp7X0SI9zCbY9jtccrKrqCpqYLu7ny6ukrIySnD6dxMRkY9drsLm20nVqsXm60ei8VIcXEx
R46U09n5Cu3te+nsbKChoYauLg+BQCVr1x5g8uQLyMoyMX9+HsuWLcXpvItbb/0cb7/9HEK8C/gx
GJYTjZaRSHSQljYbEMRi+ygtvQyDYQl+/0amTl1GRcVrxz0o9LcGXXZZDUeOHGHKlCkTOoBbSa5k
tlz8Hj1L03L0JFqPoydVOOn0VAAhxM3oq2w1JbF8KeNkEX0gEMBiiWE0FlJY+CU6Ov6X9vZDxOPl
CGFF0w6jabuYNOkCTKYcsrNbueeeVTidzoGnppoa/UJXUrKMYLCb6urX6emxYTS6CQY9RCJ1OJ0h
FiyYj9m8n4aG/Xg8tZhMR/jyl1ewcuUKnn76GbZsqSMWm0t3dyFerwOoRog/YDZnYLU2MmXKbIxG
y8DnjpwfZA5VVS1omnEgsICRE1apVUqVCbNgAXzve3DLLTB16sBmGwzbbbJu3dOnTL418myUNiZN
iuPxvExraxZmcw7hcDWBwH7Kyz9Ke3sJ8Xgu+hisELNm3YgQm2lu/jMezyFcLgtf+9oKli+/gubm
Zn7+cyuatoL09HyMxgzq6tro6noFn28/W7Z8D5iB0/lJenqaicdncuxYM1lZU0hLm8mmTc8DsHLl
CjTNQVpaOr29YRKJEAZDHiZTHtFoNXZ7Br29tdhsFmw2N0IY8fnAZEo/YT2fE8eZVKiFAc9hSQku
hBCz0JfmXNSf/lsI8VXgBSHENwdn6Rzm2MnoS/Ndi5504Zx3qmlXZnOAjo5aPJ73sVhuxGD4PfH4
MwjxDpqmD+LKyLiKYHArTqeZ0tLS444ffDGbM0cPZBoaNuLxdGI213L55Xl0dR3E693PrFklZGUF
aW6uY+XKFQOrDX7ta18mPX0dDz30AmlpVUSj6aSnryQnp5hY7ACa9gYXX/wl2tvXDVxQThY06X3O
J+9/VauUKhNu7lz9NYLBA7lHm3xraOBttxdQWfk6R45sJifHQiRygL177yMcNuL3HyEUitHQEMZs
bufYsTQikT1kZAR4/fVfYbd38MUvXsuKFdcdd90oLCzk4osr2bTpeSZPvom2tjb27atB045SUFBO
W1snsdgsTKZ2bLZ0srM/Bhxj794HaGysIRCI8NBDL/DKK1uprc1kypQv09PjoKXlN0QiLwHdmEwC
TTtIIvE6Nts0TCYXPT17MJshGu054UFBLQx4fklWy8WlQOegdUVATwcn0VskNg13kBBCAE8AP5ZS
7td/PH8MN+Nkw4aNdHdPpbCwl+bmzYTDHgyGYkymgwjRgdO5gvT0j9DZ+TrZ2ZUsX37ZCecYejGb
NWsFTmcVTU3Ps3z5ldxww7Vs315BVdUHQcBttx2fMttmsw1a1riO5uZppKUVo2lBwuF9TJ8+/4QV
B08WNI2m/1VdjJSzyVjWpxn8/a+oqKOlxce0aRezYMGdBAJtvPnm94jFDHz0o9/D67Vy+PABmpq2
EIkcJDPzEjIzP4m++GAlGRnpx3Uv9Aflu3Y10t3dTl3dfXR1dWA0ZmE25yKlAyESOBzTsNkEmmbF
bs+mtbUOrzdCevpHcLmW0Nb2B3bseBEhLsFsnkJxsZvc3O/Q2Pjf+P1/xmSKk0hkkJc3jVhsMm1t
fyUWq6Cw0ILPd/zaH+fjwoDnu2QFF3noy+oNkFLGhRDevvdG8i9AREr58ySV66zSXyELClYxd+43
2LHjYY4c2Uk4LIlGW8jIiBGP/xm/fwslJTZuv/2jIw6OGnozt1qjlJQEqK7uoqrqT6SnM9DPWlBQ
MGJF71/W+LHHXqS29lUyMvKYNm0eOTllI478Hi5oOlVrjboYKWebsaxPM3j8wb//+88oL/97SkqW
AaBppr503xeSn38p+flBsrNNvPFGB2azi2uv/XfAjs1mw+9fzM6dG7n55g/qwwdB+WquvLKEgwd3
snXr9xGihJycr6FpGXR1PUBvrwew4nRq9PS00tl5ALM5D4fjMsLhGGazmUhkMlI68PkOAGC1OsjJ
WUMi8TduvXUG06dPZ9euRvbt20hXl4fsbCtTpszkiitmH3ctOh8XBjzfjSm4EELcB9x7kl0k+uIT
YyaEWAR8DVhwOscne+nlieD1evF4AjgcPbz77jo6O3swmfIxGvX55w888E9YrXryqaFdIUMNvZnr
ufszcbuvJzdXbxXYunUL6el7uOCCC055nuXLrxjzioPDGSk/iLoYJZ9acn18ne50S01z4XbPH/g5
GPQiRAaJRBaVlU/Q2dmC3x+mq6sFu72TWKwLt1vPtWMwHF8fhgvKJ0+ehRCFRKMLsFimYzLZcToX
0NxcRU9PLjNmXMShQ1sIhbbjdl9OMOinpeUxDIYmenpaiMfbycrKJh7fi8+n59qYMSODb3zjHyks
LBwYE9VvuLFRamHA1JCyS64DPwUeO8U+h9GXzTsug4wQQkOf4jDSeIvL0VfYaRjUHaIBDwgh/lFK
Oe1kH5qspZcngsfjobm5mS1bXmbv3v10dr5HOOwmK2sF+flX4vO9h8ezjvfe2zfQVTFa/ZW+qqrl
Q7UKnM6Kg2OhLkbJp5ZcH39jnW453PfcZstGSj/d3S9RXz8Fh2MVTmcBbW1b8fs3UV9fgdutPwAM
rQ/DB+Uh7HYXfn8anZ1HiEaDeL1O4vEQ8fif6ex8l6KiBPH4EeAjeL2/ARLk5n4FTXsNr/cQfr+b
mTOzmTTJQHd3E6tX30BhYSEwugSCKs9FakjZJdellB70JTNPSgjxFpAlhFgwaNzFcvTl93aMcNgT
wCtDtr3ct/1UAU1KG+0NePAAxj173qe1NR2T6XKCwWo07VP4/ekIsR+r1cSUKSuoqnq/L/Pd2Crm
eLYKJCs9r7oYKWejsa6JMfxU9CbM5iYikW6ystb0ZcX0YbOlE40u4siRvZSV1RGJ+E+oDyMFK5mZ
AB78/t34fHbM5hJyc2/GYonidFq55RY9WHn22YM0N4dwOu/EYCjAar2QsrIIodC71NVtJj9/BqtX
n3q58+GoPBfnl6SMuZBSHhBCvAT8WgjxJfSpqA8B6wfPFBFCHADulVJuklJ2Ap2DzyOEiAItUsqa
ZJQz2cY626G/r9ThuJpgMILN9jGCwWNo2iHM5kKi0Rh+/wHKy2dQXn4lx469f1rdA2dLq4C6GCln
q7EE3cN9z2+5ZQnPPbeXSKQXn+9tzGZYvLiASCSDQ4cqOHz4AfLzXSfUh5GClbQ0L1ZrjEAgg/T0
C7BYIoTDu5k582ry8y+gqmoj3/nOXfT0PMOvfvUm4XArNlsv5eU5zJnzTXp6Gjl8+AHuuWcVS5Ys
Oa3/E7UY2fklmXkuPoOeROtV9CRafwS+PmSfMsDByGRyinZmjGW2w+C+UqPRRiJhJjt7IT09zfj9
r5OTE8RimUEg4KW0dCqBQNNpBwJjbRWYqDwT6mKknA8Gf89ra2sBcDqdHD0aIhLJISNjOjabbWAt
jtzcGdxzz6oRx1kNF6zcffc1tLa28vjjz2E0HkHTzMycqWfGjccjHD2qPwzdddffsXdvO9FoJkVF
Fw1aRsBPfr6L0tLSD/3vVYuRnR+SFlxIKbs4RcIsKaV2ivdPOs4ilY11tsPgropEIobZDKFQPenp
M7BacwkGXyKRCGCxhPD7D9Hd/fqH6h4YTatAquSZUBcj5VwXDAbZvPkvx9U1Kdvxerdis9kwGEpo
bd3T9wBwwUlbD0YKyj0eDwcPeolGL6Wo6LKBBHZeb83Ag4rL5epbX+Qt/P4sDAbVHamcHrW2SJKM
dVzD0DVGiorKqK7eQiDgITt7AZmZe2ls/B8yMx2YzVM/dPfAaFoFVJ4JRTkzhta11tYqjh79MwUF
tcTjp9ctODQo1wOH+WzatA+/vwSDwThs4JAK3ZEqK+/ZTwUXSTLWcQ1DuypKS5fT3f0YNTU/weWy
MG1aGWvWXHfKPBRjNVKrgMozoShnxuC6lp1dxt69G2loqKG7O0FTUxuf//xsrr/+mnGp96MJHCay
OzJVWkuVD08FF0lyOrMdBlf8hoYoiUQ1xcXpOBwFgIH09AymT59+RiqZyjOhKGeGns8mTHq6if37
f0NTkx+HYxUulxuPZzOvvlqH233y/DOjNZbAYSK6I1Vr6blDBRdJNNbmxcEV/7e/fZxt2+ZRXPyJ
gcDkTFays2VGiaKczYLBIC+88BfefLOCnh4z4XAtFssqEolsrNYAdnsJBQVzqajYMq6thacKHCai
W0K1lp5bVHCRRB+mefHQIT/FxRNXyVSeCUVJvg0bNvLkkweIRsuRsh1IIxDIo76+BpOpHbcb2ttt
pKfHzkhr4UR2S6jW0nOLIVknFkI4hRBPCyF8QohOIcRvhBBpoziuXAixSQjRJYToEULsEEIUJquc
Z4LL5aKsbPQ35P5K5nCcWMn6lzE+E1avXsXKlYV9A8oeJB7fyMqVhSrPhKKMA4/Hw9at7xEILKS4
+Fvk588DDpNI7EDKekymNDIzl7BvXw2trXVnpLWwv1tC01ZRXLwWTVvFpk2NbNiwMemfPbi1dDDV
Wnp2SmbLxe8BN3pmTjPwOPBLTjI9VQhRCrwB/Br4NuAH5gChJJYz5aRKl4TKM6EoyeP1eunsjCKE
G7s9D5vtc7S2HgQaEMKKpmWRSLQixEEgnPTyDO2WCAQCGI2Tycy8cty7ZYajWkvPLUkJLoQQs4Br
gUX96b+FEF8FXhBCfHNwls4h/hN4QUr5rUHb6pJRxlSWapVM5ZlQlPGXnZ2N02lCylZCIR8GgxGL
5VqE2Ek4vAkpd6FpbsrLp5KWJpLeLdDfYpqfX8Du3XtoaPASiYCm9WC11tHc3Jz060AqTINVxkey
Wi4uBToHrSsCeqZOCVwMbBp6gNBXK7sR+LEQ4i/oq6PWAfdJKU/Y/1ynKpminNv6E1bt3fsmHo9G
evoiEomjJBI+srIuYO7cZSxceBl+fxPxeFPSWyz7W0wrK1+npSWPtLRyHA4HXu9bdHX52L69Ylxm
rJyMai09dyQruMgD2gZvkFLGhRDevveGkwukoy/p/m/APwPXAxuFEFdKKd9IUllTkqpkinLuW716
FdFohKeeeoXGxufQtFYsFhMzZnyB+fMvxe9vOmMtli6Xi/nz83jllc3YbHdgtVoJhQ4i5U6mTbuY
qqqW01oo8XTLoq53Z7cxBRdCiPvQb/4jkUD5aZalf3Dp/0opf9b39z1CiMuAu9HHYoxo7dq1OBzH
L1My3PKyZxtVyZRkWb9+PevXrz9um8/nm6DSnJ6zvd7bbDbuuutObr7549TW1hIOh9mzZy9VVTUc
O1Zzxlssly1bypNPvkoo9DI+3zbMZpg5s4zS0uUcO/aomrFxljuTdV5IOfq1wYQQLuBU36zDwGeB
n0opB/YVQmjoAzM/NVw3hxDCBPQC35NS/teg7f8/sFRK+ZERyrQQ2LVr1y4WLlw46n+Loignqqys
ZNGiRaCPl6qc6PKM5Fyv9xOV/trj8fCtbz1ENHo16en52GzZ2O0uWlv3EI9v5L77vqqCi3NMsur8
mFoupJQewHOq/YQQbwFZQogFg8ZdLAcEsGOEc0eFEO8AM4e8NQOoH+YQRVGUc9JEtVh+MJj8LazW
6zEYjIMWTFMzNpTRS8qYCynlASHES8CvhRBfQp+K+hCwfvBMESHEAeDeQS0ZPwH+IIR4A/gr+piL
FcAVySinoiiKcjw1mFwZD8nMc/EZ4Ofos0QSwB+Brw/ZpwwY6DCVUv6vEOJu4F+B/wGqgVVSyreS
WE5FUZQJlUqrgKrB5Mp4SFpwIaXs4iQJs/r20YbZ9jh6wi1FUZRzWiqvAqoGkysfRtLSfyuKoign
N5HpthUlmVRwoSiKMgE+SLd9PW73PKxWB273PNzu66moqMHjOeXYeUVJWSq4UBRFmQCpskChoiSD
Ci4URVEmgFoFVDmXpdSS60KINCHEz4UQDUKIgBBirxDii8kqo6IoykTpzynR2rqF1tY9hEK+gZwS
S5eqnBLK2S2lllwHHgSuRJ/GWg9cA/xCCNEkpdycxLIqiqKccSqnhHKuSrUl1y8F1g1apOw3fXkv
lgAquFAU5Zyickoo56pkdYucasn1kbwJfFwIUQAghLgKPdHWS0kqp6IoyoRzuVyUlamuEOXckUpL
rgN8FfgV0CiEiAFx4AtSyooklVNRFEVRlHE2ppYLIcR9QojESV5xIcSMD1Ger6G3bKwAFgLfAB4R
Qlz9Ic6pKIqiKMoZNNaWi58Cj51in8NAC5A7eGPfkuvZfe+dQAhhBX4IfEJKuaVv8/tCiAXAN4HX
Tvaha9euxeFwHLdtzZo1rFmz5hTFVZTz0/r161m/fv1x23w+3wSV5vSoeq8oo3cm67yQUo7/SfUB
nXuBiwYN6LwGeBEoHG5ApxAiA/AB10kpXx60/VFgipTyuhE+ayGwa9euXSxcuHDc/y2Kcj6prKxk
0aJFoA/Grpzo8oxE1XtFGR/JqvNJGdAppTyAPgjz10KIxUKIpYyw5LoQYmXfMX5gG/BTIcQVQogp
Qoi/Az4HqET7iqIoinKWSKkl14FbgfuAp9C7UOqBb0kpf5XEciqKoiiKMo5Sasl1KWUb8PfJKpOi
KIqiKMmn1hZRFEVRFGVcqeBCURRFUZRxpYILRVEURVHGlQouFEVRFEUZVyq4SIKhSUomkirL8FRZ
lPGUSr/DVCoLpFZ5VFnOnKQFF0KIfxVCVAghevvWFBntcT8QQjQLIQJCiFeEENOTVcZkSaUvjSrL
8FRZlPGUSr/DVCoLpFZ5VFnOnGS2XJiADcAvRnuAEOJe4B7gH9CXWe8FXhJCmJNSQkVRFEVRxl0y
81x8H0AIcccYDvs68B9Sys19x34OaAU+gR6oKIqiKIqS4lJmzIUQYir6cuxb+7dJKbuBHcClE1Uu
RVEURVHGJpnpv8cqD5DoLRWDtfa9NxIrwP79+5NUrLHz+XxUVqbGmk+qLMNTZRneoHpknchyjEJK
1ftU+h2mUlkgtcqjynKipNV5KeWoX+jrfiRO8ooDM4YccwfgHcW5L+073j1k+zPoC56NdNxn0IMS
9VIv9Rq/12fGcm040y9UvVcv9Rrv17jW+bG2XPwUeOwU+xwe4zn7tQACcHN864UbePckx70E3AYc
AUKn+dmKouiswBT0epXKVL1XlPGRlDov+p4CkqZvQOeDUsrsUezbDPxESvlg38+Z6IHG56SUzya1
oIqiKIqijItk5rkoEkLMB0oATQgxv++VNmifA0KIlYMO+2/g34UQNwkhLgCeABqBTckqp6IoiqIo
4yuZAzp/AHxu0M/9I1euArb3/b0McPTvIKX8sRDCDvwSyALeAK6XUkaSWE5FURRFUcZR0rtFFEVR
FEU5v6RMngtFURRFUc4NKrhQFEVRFGVcqeBCURRFUZRxpYILRVEURVHGlQouFEVRFEUZVyq4UBRF
URRlXKngQlEURVGUcaWCC0VRFEVRxpUKLhRFURRFGVcquFAURVEUZVyp4EJRFEVRlHGlggtFURRF
UcaVCi4URVEURRlXKrhQFEVRFGVcqeBCURRFUZRxpYILRVEURVHGlQouFEVRFEUZV0kPLoQQXxFC
1AkhgkKIt4UQi0+x/21CiN1CiF4hRLMQ4rdCiOxkl1NRFEVRlPGR1OBCCHErcD/wXWABUAW8JISY
NML+S4F1wK+B2cCngCXAr5JZTkVRFEVRxo+QUibv5EK8DeyQUn6972cBNAA/k1L+eJj9vwHcLaUs
G7TtHuCfpZTFSSuooiiKoijjJmktF0IIE7AI2Nq/TeqRzKvApSMc9hZQJIS4vu8cbuAW4IVklVNR
FEVRlPGVzG6RSYAGtA7Z3grkDXeAlPJN4HbgGSFEBDgGdAL3JLGciqIoiqKMI+NEF2AwIcRs4H+A
7wEvA/nAT4FfAneNcIwLuBY4AoTORDkV5RxmBaYAL0kpPRNclhGpeq8o4yYpdT6ZwUUHEAfcQ7a7
gZYRjvkXoEJK+UDfz+8LIb4MvCGE+Dcp5dBWENAvME+PR4EVRRlwG/D7iS7ESah6ryjja1zrfNKC
CyllVAixC1gOPAcDAzqXAz8b4TA7EBmyLQFIQIxwzBGAp556ivLy8g9Z6vGxdu1aHnzwwYkuBqDK
MhJVluHt37+f22+/HfrqVQo7AqlT71Ppd5hKZYHUKo8qy4mSVeeT3S3yAPB4X5CxE1iLHkA8DiCE
uA8okFLe0bf/88CvhBB3Ay8BBcCD6DNORmrtCAGUl5ezcOHCZP07xsThcKiyDMphU/wAACAASURB
VEOVZXipVJZBUr2rIaXqfSr9DlOpLJBa5VFlOalxrfNJDS6klBv6clr8AL07ZDdwrZSyvW+XPKBo
0P7rhBDpwFfQx1p0oc82+ZdkllNRFEVRlPGT9AGdUspHgEdGeO/OYbY9DDyc7HIpiqIoipIcam0R
RVEURVHGlQoukmDNmjUTXYQBqizDU2VRxlMq/Q5TqSyQWuVRZTlzkpr++0wQQiwEdu3atSvVBsco
ylmnsrKSRYsWASySUlZOdHlGouq9ooyPZNV51XKhKIqiKMq4UsGFoiiKoijjKqXSfyuKMjKPx4PX
6yU7OxuXyzXRxVEURRmRCi4UJcUFg0E2bNhIRUUNPT2Qng5Ll5axevUqbDbbRBdPURTlBEnvFhFC
fEUIUSeECAoh3hZCLD7F/mYhxA+FEEeEECEhxGEhxN8lu5xK6vN4PNTU1ODxpOx6WkmxYcNGNm1q
RNNWUVy8Fk1bxaZNjWzYsHGii6YoijKspLZcCCFuBe4H/oEP0n+/JISYIaXsGOGwZ4Ec4E6gFn1l
VDU25Dx2Pj+5ezweKipqcLtX4XbPA8Bq1f+sqNjIihUe1UWiKErKSfZNey3wSynlE1LKA8DdQAD4
/HA7CyGuAz4C3CCl/KuU8qiUcoeU8q0kl1NJYefzk7vX66WnBxyOkuO2Oxwl9PTo7yuKoqSapAUX
QggTsAh9bRAApJ5U41Xg0hEOuwn4G3CvEKJRCFEthPiJEMKarHIqqe2DJ/frcbvnYbU6cLvn4XZf
T0XFud9Fkp2dTXo6+Hz1x233+epJT9ffVxRFSTXJbLmYBGhA65DtregLlg1nGnrLxRzgE8DXgU+h
1ho5b53vT+4ul4ulS8tobd1Ca+seQiEfra17aG3dwtKlZapLRDlrpdoYqlQrz9ku1WaLGIAE8Bkp
ZQ+AEOL/A54VQnxZShke6cC1a9ficDiO27ZmzZpzPsXquW7wk3v/WAM4v57cV69eBWykomIjR4/q
Y05Wrizr23761q9fz/r164/b5vP5PtQ5zzRV788+qTaGKtXKk0xnss4nLf13X7dIAPiklPK5Qdsf
BxxSypuHOeZx4DIp5YxB22YBe4EZUsraYY5RaYDPcevWPc2mTY243dfjcJTg89XT2rqFlSsLueOO
2ya6eGfMmchzodJ/K8n28MOPsmlTIwUFN5GXN2vC6/P5fn1JVp1PWsuFlDIqhNgFLAeeAxBCiL6f
fzbCYRXAp4QQdilloG/bTPTWjMZklVVJbcl6cj/buFwu1Q2inLWCwSC/+906HnroBeLxT+DxBOnq
qmfOnHJg9LOfxjPIVrOxkifZ3SIPAI/3BRn9U1HtwOMAQoj7gAIp5R19+/8e+HfgMSHE99CnpP4Y
+O3JukSUc5vNZuOOO25jxQqVoVJRzlb6rK9a4vFpuFwriMWguroG2M+sWSUcPaqPoRqpbiej+6J/
TFdx8Yljuk5VHuXkkhpcSCk3CCEmAT8A3MBu4FopZXvfLnlA0aD9e4UQHwMeAt4BPMAzwLeTWU7l
7KCe3BXl7NLfygBQUVHD5Mk34fG8RizWSnq63kLQ0LCfrKzgKcdQ9U9Jd7tXUVysd19s2rQF2Hja
3RdqTFfyJH1Ap5TyEeCREd67c5htB4Frk10uRUllah0R5Ww2tJUhHvdRX9/A0qV3U1TUQHX1FgCM
RjceTy3NzXXcdlv5iN/1ZHVf9M/G0oMUhoy5ULOxPoxUmy2iKCnnTN7oz6eR68q5a2grQ0vLAVpb
f8G77z7GpZf+I7CRhoaNeDydaFotK1euOOkYqmR2X6gxXcmhggtFGcFE3OiT0fSrKGfScK0MU6Zc
TH19A4cPP0VJyTvMmrUCp7OKpqbnWblyBV/5yt0nPWcyuy/UmK7kUGt2KMoIznTa8fM9G6lybhgp
8d3ChVeSl+cgEHiWo0cfxGR6jdtuu5DPf/6OEc70gTORTM7lclFWprpCxotquVDOWR+mO2Mipqip
kevKuWBwK0MiMZ1gMIjNZiMQaGbevKn80z/dNrDfWL7Pqvvi7KKCCyWljMf4hqHdGUZjgDlz3Nx2
260UFhaO6hwTcaNXI9eVVDea+ulyuViypIRf/OKXBAILEcKNlK3Y7ZV89rOzgLEHFqC6L842KrhQ
UsLpjG8Y7kLn8Xj4zW8e59VX28nKWk5X10EaGw/w2ms72LKlkjvvvGFUYyYm4kavRq4rqWqs9VNP
/OxFiN1ABlJ24vHs4U9/8rJzp+dDjV8ay5R0Netq4iQ9uBBCfAX4JnpOiyrgq1LKd0Zx3FLgdeA9
KaXK73uOG8tAxuEudIsXlyAEvPbaXl59dQ+RSDZCPEIiMRWncxUuVz6trRVs2FA77DmH6r/Rb9jw
v3R1dZGbW0Yk0p70G71q+lVS0Vjqp8fj4Z136lmy5FtkZEwmGPRSW7uVAwecdHSUsnDhDUQi7WMe
qDyWQEHNupp4SQ0uhBC3AvcD/8AHGTpfEkLMkFJ2nOQ4B7AOfXl2dzLLqCTXaC4IYx3fMNyF7tFH
7wOyMRovJhi8AKMxm0DgN5jNF9HTU4rJBFZrKZmZZVRUvHbKMRPBYJBIJEJv7x6qq3cCZgoLbdx+
+0dP+0Y/mv8L1fSrjIdkpcjOyJhMb28bGRmTgeuHrZ+DuxStVn1RudbWFhyOm4nFekkkzAP1fOjx
w5X7dAIFNetq4iW75WIt8Esp5RMAQoi7gRuBz6On9R7Jo8DT6GuKrExyGZUkGMsFYSzjG4YLRHp7
nXR1ZQJzsVonYbGAweDEYJhCIpGJ0Wijs7OByZNj5ObOob39tVOOmdiwYSNbtrRRXv4d5s/PoK3t
fbq738FkMo/5yed0Lo4qG6kyGkNvxslKkd3VFaW3dwctLU1EImA2Q3a2A5Opldra2uO+q0O7FINB
L5EIGI1ZmM29A+UYXL/tdvuI5R5roJDK64WcT900SQsu+lZFXQT8V/82KaUUQrwKXHqS4+4EpgK3
odJ+n7XGekGIxz20tlZRUrJsYNtw4xsGByLd3d3s2fM+jY0HaW9PACbsdg9ZWTPxetsBA/H4MeLx
diKRo+Tm5hKJtB93zpHGbQy9ODmdU2ltLTmti5N6ilLG20hBRDQa4cUX28Y9RXZbWzVHj0qysz9N
enoBx469TnX1n7BYDnL//VZuuKFmIIAZOnbIbM4gFvPQ01PB/PkLsdvtwAf1G+BnP3uE7dt9FBd/
6rhy9/Sso6qqhczM6zEaJ5NImE7Z6tHZ2Tmqh5XTudEPPWa05zgfu2mS2XIxCdCA1iHbW9FXOj2B
EKIMPRi5XEqZ0BdRVSbS6VbA0Tw5DK5w9fV+WloeYNq0ChYsuJNAoG3Y8Q3Z2dlYrTF27HiFujqB
15vAaLSSSAQxGAIEg1lYLEFyc4tobOwlEtlMJBIkKyuTvLzcgXMGg0F+9KP72bu3lVjMTno6zJ+f
x7JlSwkGg+M2UySVn6KUs9dwAeuGDX+kt7eW8vJ7k/BdsyDlDMBNe/sR2trsRKM3kkjAu+9O4dCh
N4lGI9x1l76iw+CxQ+3t4HYfw+9/h5ycCwiFfPh89TQ1bcbtbuc//uO3VFTUYDYXYDK9R3Z22UD5
X3vtF9TWegmF5iBEN3a7iaKibEpLCzh2bPhWD6MxQHNzE2lph5g8edHAv6A/mLHZbKxb9/SYbvRD
gwOrNYqmdRGPOwmFjKc8x/n4gJEys0WEEAb0rpDvSilr+zdPYJHOS/3BhM1mY+vWbacVaY+2m+N3
v1vHpk21TJ58E0uXzqay8nXq6jYTCNzDvHlzhx3I6HK50LRO9u/fTCh0PVbrEqQ8QizWhNX6Fnb7
arq6arFaC8jJcWEwNBONvkRBwSRstiMsW1ZCNBrh9tvv5dChKBkZbkpKSmhq8vDyy3/hySffZsaM
3JNenMYyU0TlrlDG20gBa1dXPQcO7GX+/Jzj9v+w3zWv10tu7lTS0spobNzDsWONxGJl2O1FmEz7
MZuX4PU6eOqpV7j55o/jcrlOGDv0wfXk+YGBym53O21t+djty7BYurFY3FRXvwZs5MILb8Nuz2XX
rp20tRkxGtux2bIJhTR6errw+Q5SVqbXxeFu3H7/fVRW/o5oNIbZnEsk0kZ39+usXFnG1q3bBvbP
ycmhra2GDRte52Q3+qGfsXPnIxw4cIxp0y5n9uxLiETa2LRp+HOcrw8YyQwuOoA4Jw7IdAMtw+yf
AVwEXCiEeLhvmwEQQogIcI2U8vWRPmzt2rU4HI7jtq1Zs4Y1a9acXunPM0Mj8+bmGvz+BAsXrqW4
eOaYIu2Rkuj4/R88OTz88KM89NALxOPT8Hheo6iogcsuW0VJSRHB4B+4664bcDqdBAKB44IZj8dD
PJ7FlCnZHDy4FSnfx2jUcLuvAipJS9tGOLyfaDSB2+1g9uz5LFpUxLJlS7FarWzc+ByvvtpOa+vV
5OQsQ9OC7NnzS8BLVtbXCYV6MRhy8Pv/m8rK32E0mj7UlNBUzl2xfv161q9ff9w2n883QaU5Pedj
vR8pYM3NnQtEaGurwenMH9g+mu/ayVoos7Ozycoy4nJlkJ2dx5Ej7aSllWE0tiKlCYdjBibTJBob
nzth/MXgsUODgw2An/zkaQoKPk5GxnQOHtyJEMVYLFdSU/MHioqWsHv3E3g8RWRmlhONekkkDPh8
vdhsLRw58jqf+tQlAMPeuOfNu4e33rqXiorvEonYsdkifOQjJSxd+kl+/OOncLlu4tgxaGioJhKB
WGwyjz32IsuXX3FCLpyhwUEg4KGzsxchlnHggMTjqcVuN5KZWcq2bbtPOsB1sIl4wDiTdT5pwYWU
MiqE2AUsB54DPUro+/lnwxzSDcwdsu0rwFXAJ4EjJ/u8Bx98kIUL1YzV0zU4Ms/JyeHdd18kHK6l
vb2GyZOXjCnSPlkSnS996aKBJ4d4/BO4XCuIxVr7VkncSGnptVRUeLn//ifRNNcJLSZer5dQyMTF
F3+RYHAn8XguDscMhDDi8z1IWVkZF1wQ5xvf+CxOp5Ps7OyBZtOtW9+joqIGmEQ4XEdW1ioMBguR
yEJgN1brVHp6qjGZClm4cC01NT+mt/f3tLUJjMYQy5fPPOlMkeEu0Kmcu2K4m3BlZSWLFi0a4YjU
cz7W+5EC1kjET1GRhe7u12ltzRrVd200YwGO/w4vRIgA8fgeEolKJk0qw2RyAYeByCnL3h9s1NTU
DNxwE4kgmZk+9u17kWg0nVisjuef/1d8vgZsttVMnXonnZ0v4vNtIx7vJBQ6SH6+kWXLlo54425r
g+7ubObOvYK8vAVomhGP5y3+9KdN9PSAzxfi8OEgFst0zOY0IJfa2r/w9NPPcO+93zjuXEM/Ixj0
0t7eSCBwGULkYbdPRYgITU3vEgw2nBAspNIDxpms88nuFnkAeLwvyOifimoHHgcQQtwHFEgp75BS
SmDf4IOFEG1ASEq5P8nlPK8Njcw9Hg9GYylW6zwaGl5gxgwPdrtrTJH20CQ68biHcLiJlpZCjh4N
U1BwEx5PkFgM0tP1CtfQsJGOjggtLT7Ky/8et3v+CS0m/RU1Emln6tSpVFd3Ew7HiMcP931GgpUr
L2HJkiUDZVm37mk2bWrEYrkBi6UbTXPh8fyJlpb15OTcipS5RCIm6up2I0SAnTv3UVhoZ9KkMqZM
sVFd3U4sZqOqqoUNGzae0DV0qgu0yl2hjKeTBay33XYjZrN51N+10Y4F6P8Ob926FbP5HYJBC5Mm
fQSnczk9PXvw+f5McbGV0tLSEcs9OPjWx05F2bnzEXy+MC0tXvz+HiANkykDKAF6sViyCAa7ycy8
jszMZcTj7XR2PkppqYWCggKAE27cPp+Hd99dRyAQpKGhA49nO0VFZeTkXMXevX8kHo9SW7uPUGgp
XV0x4nEfiUQ9ZrONqqomPB7PKYODUEhf58diycZqTcdkMhEIWOjqOnH9nxMHuOpdMd3dr7N69bmb
HC+pwYWUcoMQYhLwA/TukN3AtVLK9r5d8oCiZJZBObWhkbnNZsNshkQii0hEj9TtdteoI+3BSXSs
1mwqK5+kubmbrq7J/PrXW8jJKeKKK+6hqKiZ6uoaAIxGN21tHbS27mHGjIsHZo0M12LSX1Fzcj5K
NCo4fHgzPT1vUFraw+rVlxx3IT1+jn5/8+s0srJupLPzD6SlXUYwWEck0obNFicvbyYmUyH79m3B
YnmHYPAyiou/MHABH+7Ce6oLtMpdoYy3kwWsNpttVN+14Zr7jUYbDselJ+SCGfwdnjHj1zz77E6i
0WZ8vp8BfpzODm677cZh81XY7XZ+97t1bN++l1jMhstlZ+nSMqCDAweOkZGxhmg0G4ullWj0j0ye
bGb58i/yyiv30dLSgM9XgdHoxGQyYzQ2YDS2sGzZDQOfNTTQ2r79PjyednJyPofL9XFCoXqqq7cQ
jQZwOOyUlIR55ZWXicfzsdkWYDC0Eo3uJJHI5/DhFmpra4/7vxsaHMTjMTQtRij0Kg6HDSGc9PTU
E4tVkJ1tHfH3FY3+gaee+hGNjUEgQmGhlUikaKDb+FyT9AGdUspHgEdGeO/OUxz7feD7ySjX2eJM
zIseGpnb7XaKirKpqqrAZvNgMBgHViDsb17tL9fgc/SXrz9Yyc8vYOvWX3LwYAux2JVADkK8hM/3
FunpW1m6dBWRSBX19e8SCBxFiIO43RYWLDj+azG0xeSDC+vzOByweHGIuXMv4DOfOXHtEK/Xi8cT
xuXKAKCoKJvq6hocjnzCYY1jx9YTDu9CSj+JRBvhcCGRSB2JxF58vk5ycm486SCs/gv0aKbKDc1d
4fF4qK3Vxy6XlpaqgOM8NtZ6fqqAdTR5Uj6op7ns3v00DQ01RCJgMESw2Q7S3Nx8wjlcLhff+MbX
KSrayNatVXR2+nE6bSxfvoLVq1cNO6vi8OF3qKuzYjZPxW430tlpoaFhLz093cyc+Una2uIEAnsx
mexkZV2JxXIQm82OxRIhHH6fjIzZQC7B4CFisY3Mneth2bKl7Ny5E4Dly68AtrFt2zO88soeamra
MBhuIhTKpqOjnpyccgDq6n7NRRfZWLFiBU8+uZZgcBOJxN/QNHC7y0gk0qmv/wH3378eTXMcN4Os
/zMqKjbi8QRwOAROZxyb7TV8vm2YzVBYaGHKlJnDPnzZbDZMJjNpaaUsXryY3Ny5RCJ+tmzZgtl8
bs4YSZnZIsrxzuS86OGaWXNyomRnv0NGRivt7esGnoxuuul61q17mm3b9rFvXzVdXWGyslzMnl3I
FVeUs3r1qoFgZceO56muriYa/SSwGCl9SDkPKY/w3nvPEIsl6OnJIBBoIhrdxmWX5ZCePoVAoI2M
jLyB8g2eD19TU0N2dvaoWgKCwSAvv7yVvXv/H3tvHh5HfeV7f2rpfZO6ta/e9w1jjG2CWUwCOBCW
hCWBTCYhk+fOZJKZ3Jn7vjP3vTczd5KZzGSdDNlD9pgEAybGjm0MAmMjvCHb8i7JkqxdLam71Yt6
rarf+8evLeOFLQECXJ/n0dPqUlV1qavO+X3P92xHMc1ncbsbCIVcVFWl6e3dQKFwCF234fcXUNVG
JiY2MjS0mWg0T11dKaZZi91ecc45zwc6g4ODHD58mmx2FNPMYLdzQanc+d6cy+Vi27an+fWvn6Gv
Lwvkqa93cN99H+T+++99T3oxl+Ti8sfq+R/TbO2Mnh48+DOGhlQ8njsJBBqJRg+QSAyyc2czNTU1
F+jYWWBz0wV/OxOCPMPivfDCtzl4MEBJyQepr7+DbLaHoaGtBAI5hoeTXHllkMHBPvL5HPm8Rjab
Z2LiIENDB8hmbZSWllJefohs9iVSqRMUCiZdXXZuuOEzCJHH46mnsdHD/fffwMKFlbS11RMKNaIo
txONGoTDo5hmAa/XTzI5zPz5K6iurqaxcSqjo+W4XJfj8SzANJP093+ZfL4RVb2D6mpZvfb005v5
1a+eYdGiBVx11Uy++MVPT9qVpqY4gcBKbDYvhUKKeHw311wz76L344wT0tDwkcmW6K/W5fS9IJfA
xTtU3s666EgkwtKli0ilkrS2nqVZP//5VaxZcw2ZTGbSgJwxHuPjXqLRJej6VUSjObq7U4yPn53b
sXhxFZs2PUE+70SIaahqBEU5gqoGsaz7SKX+O21to/h8CwkEAgSDC8nlTAKBIcLhs813+vpeYmho
O5WVMb70pR9jGG50PcuCBeV87GP3MHPmzFf9Dpua4lRVLefkyf2MjCRoa2tDVUew2dLYbAWmTl3F
4GAnyeQM/P6VFApJhEiTTB7GslrI50eQPd0gnU7T19eKzZad9E527mxmeHgct9tDMLiCbDZOW1vH
OaVy5y8gPT3H6ekZA+6mvHwNME5v7xP84Afbsdvtr35/hYCjR+Gxx2DpUrjtUgPbd7O8FXr+elmQ
UCjE4sVVbN++Dbf7b3A6Z5HNxhHCRkPDzTz66JPs3ds12QfmYome5zNxF1ZVpNG0j2CaIYSw4fUu
wrKy9Pf/E/F4lN///ofkci5UdR5CXI9hHCeZnGDXrq9hGCXMn/9XNDbWcurUYwwMLCOXm8XISBRN
U9H107hc5fT0hPjOd3ZTUhJh1qzPk80+ixAF7PYaxsYsIpGTKEqS6dPt3HffPbhcLubNm83p017i
8RbS6RZUNY2q5qiouIX6+mW0t59iYMCFpq0hlWqhULiejRt3A8/ziU/cR11dHV7vBpqbn50Eha+W
2/JKXU6rqmrxeAoXhGLeC3IJXLwD5e2qi76Y13SGBqypqbnAcDz99NM88cTzuFy3Eo+34Pffide7
iFQqTCJxgsbGepqbt3LLLZK2DAQeZnh4HPgWlqWjKC4UxYtphjFNHU0rw+XSqKlp5LLLPkE02kEu
t56rr3bxxBP/xIkToySTMUxTRVH8lJbaqaycTi7XyHPP7WXLlt188pN3XNTLe/l3WCi0oKrHMc1t
mGYZlnUVTmcJqjrG6OgEqVSYXK6CXG4XQtiwrDiKkqW83GJ09ClsNp3BwSxdXSdJpXbR0CAnr65d
+wFaW4eZNu1Khob2kc2GcDobSacLnD69mY98ZMU5gCwUupXR0SRHjthJp0/hdI7h9fopL5+GpjlI
p39MU1Mrt9xy07n3Vwg4cgQefVT+tLWB3w//9E9/9DNwSf508mbr+Rl9luGKTDFcsfhVWZDVq6/i
V7/aQzY7QTy+B7sdZs8OkstZHD2ap7r6ahobV78u0HOxqgrL0nE6Z5DPj1AoZLDZ3CSTrYyPl+Jw
rCQer0GIMizrAEL8AkUxUdU5RCItlJen6OvroL8/zuhoN273naRSOaACn28VqjpGPr+Bysq1JJMZ
4vGNLF5cT339TNratuP13ozHU8HY2F5qak7zyU+unQybXnPNPMLhNkpL5+DxVDExMUwkcprp0+dR
KGQ4dGg9yWQWy9IQooOqqv1MnXodzc1bJu/LG8mjOr/LaSDQSDbbw7Fjv8Lp3MV3vmNiGM73VOfO
S+DiHShvV130xbympqateL2HWbhwISAN1q9//VvWrfs9XV1xolELr/dhNM1GQ4PM1nY6A8TjYLdX
kErJ66upqWHOnFmcOrUdy8qiqvehKDMwjEPAesBHWdk/43QqdHfLuOOcObfQ26tTKBRIJCowjCA2
WzlCLMGyHESjQ8TjHVRXC8rKPsvIyC9Zv76Nlxu881sAl5f7GBzsoaLiLzHNLTidNwLVlJfbGB3d
i2XZyWafRlFsCHEdQlSiKN3YbLvx+8u55hoPW7Z8k87OPB5PGcGgTiRSz4MP7uXxx5tRVZXly7+G
3/8ifX0bit9DDr8/xerVV52zgAwNQVdXHkVZgKbNxzR3F72YPOXlNYCPWCwp728wCK2tkqF49FFo
b4dAAG6/Hb7xDbjhBnA4/uhn4JL86eTN1vNf//q3/OAH20mny1AUH0IkOXZsM/l8nr/4i4unt9XU
1LBo0RTy+XJ8vhmTC9qmTb/B56uivn4VTmfgdYGe83O3XK4gbrdOPN5bDHukUJQso6P7gcX4fNXE
YkmE0IBqFGUjDscNaNrNWNYJVFUln+/G6Qximj5iMcjnY9jt5djtQcBDNguaZqJpNWQyFocPP8Gc
ObcCsvoskYhht7dxzTVn8iakTSsU8kxMdHLy5DEgT1UVTJ3qpqbGSWvrI4TDSRTlw1iWF6jlyJE+
dP0AweC59+X1hqWi0SiZjIVhzEDWNjiASlKpBKlUHap6Bw0Nc95TnTsvgYs/sVyMwnw76qJfr9e0
fv0GfvCD7cRiswgE1pJKDZFKJbCsx7HZdjBlykfIZuPY7ZDPj0xeXygUYuXKOWzduhfTnI5pRoA4
MATUo6pZQOD1LgakISgtbUXX07S0xEmn56FpA9hsd2BZlYBGLncAIaaQTu+moqIMwwjh919Oc3ML
a9b0n9NR9EwLYMM4VKQgvZimDjSiaQK/v4Jk0kU+n6FQ0PF4lmG3X0E2G6GsbDlOZ5BU6iTXXns1
R4+Gqa6+mnh8gO7uOF7vzbhcLsbHnyWbfYGjR3/L6tX/yKxZETKZKKnUEDabYzJeLUFOOX19bfh8
s0mlOsjlbBhGDiEiDA7aiceP4LD3saAgqP3e92DzZjh1CkpKJKD41rckoLDb/+h7f0neGfJm6nkk
EmHdut8Ti80iGLwXp1N6xtGodAzuvPNDF10Ez+Zb7cDlcqGqjfT0tJJK7WLRoqtwu88e81qg52K5
W4GAg8HBTVRXL8UwmhkZeYl8voOysssRogxFMZBhxxkIcRzDWEqhMIIQUWbP/iw2m4/u7r3IbgQ1
aJoXm01gGHEgjKZBLmcyMnKIXC7Mnj2bOHhwH42Ns5k9ewnHjv2EkhIvHR0m//IvD50zf2Xu3P+X
xYvPloXW1IQZHNzIsWNdGMataFo1ijKMw7GSXG42hw+v44Ybqt7QfTnDJm3ZsoehIQGojI29gMdT
iq4ncbkU7PYb8flmYFk2dL0Wv//aSQb43RwiuQQu/kTyaolcb0fjpdfjfK6oYgAAIABJREFUNQE0
NbWSTpcVBxYtolA4TDg8Si43nWj0dzgcXoSA2toUiUTnOde3du2NfP3rG4lEGhCiFtgN9AIFFCXK
yMhDqOrnUFUHsVgvx479iIUL3XR1pcjn61EUBzbbdBQlhWXZEUJDUWowDEEi8RKqGsfnqyWVamHd
ukfYu9eYZGHC4VZGR7/K6OhjmGaAaLSFVGoQ0zyExzOHcLiPUMiHrseIRNJkMkmy2ZPYbH4SiRQT
E6NMmVJKPB7HMNxUVCygvb0Fj+dOHI4ZZLNxNG0aNTUuuro20Ni4k8rKxRhGhnh89znfg9cLIyMy
Ez8QqKS0NE4s9jSm2Yuq6FwmdvKRxM+50zrCtKeysK8U7rgDHnwQrr/+EqB4j8qbqeednZ309eUI
BO6Y7Bvj9S7CNHP09/+fCzpnvlzOL2u1rDg1NSO4XFVEIh1FBuL1laKff64pUwo0Ntro7Gyiry+H
qoLHkyOXewGn814ghxDtgA1QKRTaUNUXgBQTE2NcddUnyOeTjI21Eo8fQIhpFAoWhcIgqtpFSUk5
PT2byWYPUV6+FqfzJmKxo7S3NzEy8gg1NWuYN+9ThEIzXnH+SmlpNeFwCbnceubNy7FrVz82WwbL
asHhqMXrnUsm00k8Hmbq1BlveGjh+vVtOJ0r8fn2IUQjhQJUVzuYOrWMHTscuFwVdHZ2Ew6nyOdB
01I4nd2T1Trv1kmql8DFn0heK5HrrW689Hq8JhleyKAoPpxOCULKy+dimgXC4dnAT8jlvkpVVT1T
p9ZPVoucEafTSTDoR9OCpFIHyeUyWNZHURQvivJbksk2kskvYpoC09xPOFzK8eM+DGMcaEPTGoBO
7PYGJiYGgTSm2UMu18PAwCk8ngmamr5FIDBEMllHWdmnCAZncuzYBjo69hGNOjCMk6jqOPH4MKpa
i6q+hGXZGB1N4HLFqKuLMj5uIxZLI0QMRUkjRB7T7ENV0wCYZozOzt2kUjksK0kqtY9cLoOqxqiu
rqWy0kc6/Si9vc9ecJ/OLCDr1+/AMGqZmKjFbktyhbKRO5ST3FHYxnTSxFQbzRULeWLRLP78F98i
VHW2WuaSvHflzdVzO1By3raS4vZXljPVH2vW9LNu3SO0tsYZG4ty/Pg3cLmmUVlZQXl5AJ/P5M47
Xx30XKxEdvPmbYyMdLJixbUEg1PZvPk39PXtQIivIdscjQNZYBR4Bsty4nDMY2Cgm4MHf0F3d5zK
yi+h67sYH9+DojQDMex2FdOswDSHKS+/ienTv4imuaiuvoLBwQCRSD+zZt0zOR/oteev6KxYcRmP
PXYYh6MG0wySSIyTyTQjRBceT4obbrjudd+N/v5+fvazJwiHq9H1dlKpUQqFH+H3f4KxsQnKylIU
Cj3oeh/d3SE8nrkEAgGi0d2Mj8d55pkdHDhw+F07SfUtBxeKonwW+Htkw6xW4HNCiP2vsO8dwF8C
S5BBqWPAPwshtr/V1/l2yusNSbyVjZdezWtas6ZqkrkoLXUhRJJstqfoEakUCi4gjt9fwpIl01i5
ci733Xdhj4kzxxtGC4VCHKfzfnI5B6nUPwMxDMMDvAR40bTrMIy1qGodcJBCoYlcro1s9nvo+h1Y
VgJFOYFlHaZQ6MfrnUUu10g0GqW/f4KTJ3dRV6ej6z9kYGCEXC6EZZUihIGmWYRCUSzLRyJxklxu
T5EtSbJy5S2Mj1eQSPRjGLMwTT+QxDBOcOpUB//wDz9hcLCPTOYl8nk70Ijb/QEUxcLrzdPdvY/G
Rosvf/nzwFmvrr+/f/Ke3X33nSAeZ/d//YrFHV9lbbqPRitDRHHwpF7NlyoWEvrwt7G5g/T2fosP
JZOXwMX/JfJmNVibPn069fVOenqa0TQ/TmeAbDbO+HgzjY2uV+yc2dHRQWtrK4FAgPb2TvbuNRgf
r0BVb8bvbySZNBgcHCceb+XGG/3cffffvaInff72l/eBaWi4k2BwLlu3biccrkeIW5G5V+NAGjks
WwVCKIoJTDAy0otl5fH7P4+qNuB255k//woCgTiWtZ1Pf/pDnDx5kv/4j6eoq/tbNE0uuDabm0Bg
OiMjXizLf87/e7H5Ky+vAlu0aBGNjR5On24CrsCydAxjANPcSUWFSUlJyWQ5/Gvdp4cffoTOTi8l
Jfdgs9USCAwxNraOdPr7ZDIaQjSyenWI55/fj8czH6fTSTbbjhD7mDbtSjZufB6PZxENDdIBHR4+
ybp1m0ilfsFnP/vf3vAz8nbLWwouFEW5B/gG8BnOtv9+SlGUWUKIsYscshrYDvwj8qn7FLBJUZTl
QojWt/Ja3055I4lcf0wd+2vJ+V6T02kQCsVoaSmhuXkdXi84HBM4naNEo7/FNHNEIhZjY3vweDpZ
vPhjVFdfyd69W6mqev6cBKRIJEIsFmPatHogRyw2jKJEMIyHislmn0DizW8AAtO8Hk1bST5vQ1H8
CDGBqk4gxC5M8xCq6qCmRkdVc0xMLCCbrUaIq9D1CizrKNnsk/T0nKRQGADW4HQ+gKo2kM+/RC73
BMPDu3G7aygtfR/l5WvJ5cYZH3+QeHycXM5DLlcgn38Sw1CxrBRC2MnlShHCRyj0j5jm70inn8E0
96NplVRVLcDnyzE+3g7kzplhMulpeAQfKMlyzcgw9z/3HJ/o6yNus/Oko4pHeT+7HR/FE1BxOPYw
t/dFqqsX/smHmV2SP438sXoeCoW4//4b+P739zMxYZJOy3k+weAB7r//hgvOHY1G+bu/+0e2bTtK
MmlHUbKoapy5cz9ILufA5/swmlZDNtuNYZzEZlvByZM7+cEPHuLEicg5nvStt97Mpk1bL/Cw16y5
hj179tDTE6Gx0UdT03McPTqAYcxBAgkXcCMwBelkdAIWQjRiWQOY5gtkswJFOYjHM8jUqbU0NtZj
t1uMjrYwZcoUpkyZwne/u51odDclJfOx2YKAi3i8E01LoaqJc/7vM/NXIpHtHD9uEosp9Pd3Tnb4
ffHFfdx11/v52td+SSRyBF2fjq7r6LqPdNrD5z7379TUzHxNFiESiXDo0BCmOZ+hoQSqaqBp4HBc
h822jfnz4ctf/iuy2Szt7f+HbHb7ZDOu2bNnUlu7lG3bXmT58msJBudy7NgJ+voyJBJTefDBJwD4
1Kc+8Y5mMN5q5uILwA+FEL8EUBTlvwEfRIKGr56/sxDiC+dt+v8URbkNuBXJerwn5J0yyOZ8r0k2
hvFRWXkzFRWSyRgY2MzcuSk6Ow8xNNRSbJoV4PLLb2fRonux2eTDfYZxOX+BHRwcIZlM4vUGUNUR
kskMmvZx5Iy6AQzDB3iAWiwrg6J4EKIMIerQdT92ewOBQAU2m0owGCYYnE9Xl47bfT3JZA2Fwjim
OQNVvRvDeAQhEsCHMIypwASKshBFcWFZ3SjK1WSzCTKZdrzehUAjHR1j9PWdRoi70fUaTFNDUaoQ
4jim+SjZrAfLGqGi4s/I5XpxuSrJ53+PrregKDpz507F41GIRqNs3ryNJ3/Xy5VMZ3lfM3OPPkJl
bpyI7mRzeR3PzF/J1lQZqr0Om60Cf9aktHQBpumlvf2XFApt3H337HdVXPWSvHPkvvvuxWaz09R0
hFjsGKWldq68ciFXXrnsgnkZf/u3/4Pf/W4My7oft/ta8vkBksnfcPToS5SUNOJyeYnFcmhaCNM0
Mc06jhw5TSzm4+qrP3/OqPIXXvjfRCINkyHeSKSN//zPb/CVr/yMVEpndDSMZbkxjCBQBjiBweLv
85AgYzGwFNgK1FEoFLAs8HqT5PMHyeVUolEH7e0LEGKYUKiFbPbDzJgxg6qqHPv2fZvh4VkIITDN
ApYVpbQ0QXv7I3i9nsmci4GBzUydGqK7+yQ7djzHxISXQKCSRYtWUV+/lPXrt7FkiUFtbTV2+9VA
CJfLh6YdJxotIxyeyeLFa8nnR1+1qiMajdLVNYZpLscwanA66xEiy/h4HFXtYeXKm5g5cyaRSIRF
ixZQKFyP11s9md/S1rYJsFNRMZNjx07Q1pbA45lLKDSXSOQwGzd24vW+sytK3jJwoSiKDbgc+Lcz
24QQQlGUZ4CVr/McCnIUe/S19n03yTttUuaZz2ttHT4nVKNpczl5sp329heZMWM6Pl+YoaEJrrnm
a1RUzJo8/uWMy+bN2yZzSaqraxgYaCIcfoRc7kVyuQ4KBRVdtzDNUwgRASygAIwWQUUEyAG9FAoJ
XK5GQqHPEI8fpa1tPZa1hUJhDkL0YFnDgIKiKAiRR1FyxXPtoVCoRVE0bLYaoArDsKOqQXR9GWNj
v8Sy2pg5cxGpVDOp1DD5/BZMsxJFKcGygsjKFoVc7goGBp6nvDyEqnoIBi9HCJ1ly6qprp5OMjmA
ZfTjPHCA2q8/yI+7TxOcCBNzBNjmmsvW8ttpKvhRVB3G27EsQWXpPaTTzxAItBQZkhT5/ACrV0+5
NMzskvzB8nJnYXBQdthsbR2mufnxc1iGH//4pzzxRCvZ7G3oei2GkcXpXEo6nSaT+TGWdRJdfx5F
schkWjDNHBMTCSwrwshIA11dGcbG5KjyXK6KAwee4oYbbi8OPezg2LEnOH3aTyazEE27jHz+98BJ
JJCoQg64fgmYC4SQuuYqvt+J1P9yTLOS0VEFmy2BZS0BDgJNCOFkeFjjr/7q35gzJ4jLtYrGxjJ6
ewW5XAJFOUBVlc61136P48d/TEfHN4lGGzDNGKo6xvDwLKZOvY/R0Q243bMAHSFmMjrqpKurliNH
1qOqMHOmzowZ16LrghdfPEhp6YcxjAksy/6KLf5fLuPjEYLBIEJUE48nMU2ALA5HlrVrPwC8fC3Y
jdN58+SohURiP/X1TuLxXvr6Mng8c/F6K2H8BQK+Empr11ww/+WdJm8lc1EGaMhg2sslDMx+nef4
H0i3dv2beF3vCHkrEjb/mKzii4Vqjh07wcCAFyGmU1PzCQqFFKdOfZMTJw7j9YbIZKK4XEGSyQG8
XojFYmzZ8hJ+/71UVi7i0KHDjIzUEgp9BtNcTyp1lHBYYJpJhChHJpsdA/YjxzULwAucAJ4Dukkk
ejh6dAwhPMjENBuQKV7hFcBp5EDdFEKEkB5QBGmEbiafjxYTwDIYxmkymQkUpZeGhinU1Cxm//51
FAqzEOJ6hChFRut2Ix/dcoRQsawSotETOBxJJiZ24XYvJFS6jIr2Taw++hDXRY/jeSiG1+nlxLyP
cnjWLfz4xB4i40uZmPASjw/g8SzC55tKJvMIQnjx+T6IEBtYtWo6Y2Pd2Gyz+PSn//wdTXNekneH
hEIhNm/expYtgzidsklUoaCzceNuduz4R154oYtMJoBlTcc0BbncCaAXIV4C4mQyFvAtJLv4YXS9
BgkGLKLR0xw8GKah4UoCgQCRSIh4/HE6O5+jtfVReno6SafTGMaNgA9FcQJXI034s0gCulC80vuB
JLKCrAxZpj6OTLkbBYJY1lJyuWPAVhTl/cAwbvefo2l+OjoOcfp0CzNmXMett67lySefJZutxuW6
Grf7WUpK6pk+/W7a27/PyMhpEgkXiYSJ13uMTMbF+HgPhuGmUDBpbt6FxzOFqqq7sax2DCNAZ+cA
Hs/z1NcvJ58HXS/Bbp+Y1NHXKs0tKXEQje7B768gEKhhYqKTTOYk5eWVOJ1nB5xdbC24++7ZGLlG
9v7sJ9zUl2MFeeYn9zEt28Xnrvt3PJWL6e199k3refRWyDu2WkRRlI8B/xv40CvkZ5wjX/jCFwgE
Audsu9js+neKvJmTMv/Q+QTnj0B+eahGJjlF0XUHLlcpJSWNuN0hGht3cOTIdxgYeBZdL0GIJLo+
wOzZDv7t3wY5eDBCaekoIyMvMTAQI5t1kk4bZDJRVNWJrkcxjHXAdCSQMJF4sxM5NNeFBBB1QBDQ
EKK0+Hsl8pE9CbRxZiyzzP09jvSCViKN1YtI+jWLEL9D02zkcicQ4kV0vY1EopH+/ggTEwqqegNw
M5blRYg04AZ+BZRhmpuwrF50fTF2Ha6zHeDW5Faue+gLBDNJ0iUl2O+9l/jatfzDxv2oto+g6y7C
YxtIp1cD1ahqHpttCqlUGCEgmTyE37+MXC7P2Nghcrnj3HTTwrfdSPzmN7/hN7/5zTnb4vH423oN
f6y82/T+zZJXcyT6+/v5yU8e5dQpQTYrm0T5/Q5qambw4ov7UZRVaFoa0yxDLuqtQBMQANYiF/8X
gYVIRrGAqtYjxDIsazv5vI7DEUTXbTgceez2Eg4ceAzTXIYQN2OarcAyJOBvBcqB25HgYiXQARwB
1gEzkfoeA7qQuRjNwCmkzueReh5BiMPF8vRR7PZVZDJdKEqQwcExXnjhGcLhDLruI5VKUyjsJJEY
YnQ0TyLRja4vwuX6KIZRQirVy4EDT2EYMTye9+NwzCWVakZVD5NIbCYYdFFZ+T5OnOiivX0PFRVz
MYwIqVQzixcvxe12AxeGsc+3p7LFuEY8voF0Wva8q6i4cLjZmbXg1pXtZHfsoKStDfevfobYt48H
kklMoM1eRot/Ck/OfT+VS+5n4A8Mob+dOv9Wgosx5MpRed72SmD41Q5UFOVe4EfAR4QQz72eD/vW
t77F0qVL/5Dr/JPKm5Gw+UbnE7wSGLniika2bj0zVthHItGJogxRXz9zspmOyxXCsoKY5kJUtZZE
ooNEYh/9/dWUl6/Ask6Qyzlpa0sQjfagqrMAJ6paTzbrBaaiqjOxrHqkQXkamS1+NdKgeICPIenR
euA+oBbp4WxFsh1nysgeRrIU9cVt1YCCfMTiqOoGLGsMmIVl3YamOTHNDoQQHD7cxNy5PgqFCioq
3kc0asMwBNLQLQY2Ae9DxclVop378pu4fWyEynCOQkUFQzeuYeLuu6m/5x5QVQLAqmiCjRu34nDM
I50eQQgLVXXhcOjouoUQKSwLpk4tZ2BgJ4XCYWw2g5tuWvwnCYdcbBE+cOAAl19++dt+LX+ovFv1
/g+RSOTccMcrORIPP/wIR4+qmOatuFzvA8aJx58gkdjHxITKtGn3Ypr7GB39DlJnVCQ4nwXMR9fH
MYxyoAZwI8RSFKUMRSlFiGfJZB5lfHweNluEROIJVDVNLqehKBVIYD8ObAYakFHtaiRDaSBBx/uB
PcAzwBNInfMiGckEMAe4G/gA0vHYjGQSJxDCRSrVj832M0yzB8sKE4vtYGDAjRBBTLOUdHo9luUm
k5mFYTiBBIqyFqjDsrxYVhWFwhCquo9CYRjTrEFVp6HrPmKx7zF37k1cdtlKFEWjre1JhoZ+RmXl
EMnkfsrLF5LNxs8JY7vdbn7xi3UX2NOVK2cwPj5CY+P1Fw438/vhwAHYswd274Y9ewieOiVvdEUF
rFyJ8j//J6xcyU9aDvLYtgFqa2+lsnLxHxVCfzt1/i0DF0KIgqIoLcAa4EmYzKFYA/zXKx2nKMpH
gYeAe4QQ296q63uvyB8yn+CVwMjatRXcdlsdzc0bGBpKYJpHqK1dwfz5cuFLpyP09JyksvKDXHXV
ao4fP0AmU46uL0ZVl+F230gqFSUefxa3+yomJibQtFEM4wCm6UKIceBDSCNTgfSadCRbcQ/SAHUC
u5BpNtcCy5EAwglchozXnmE7DKQxshX3TwDtgIXdruH1rmJ8/Fksay5CJDAMDV2/BpttEZq2gaGh
cQyjh5oaFV13MzAQoVAQKGKcqxnjXnU7t4vjVIkoQ5aL/VNnk7v1A2xPuklOKHifa+Oq/G8mDfua
NdcwPPwIu3dvRFEimOZ2AgEXmuYjEtmKECfxeAKUl9txOAa45prreOCBP3/H0pqX5J0hL3cGWlpO
Mjw8xrRpK1m+/LOk0yPnOBKRSISWln4sazl2+7U4nXLonqo6SCQ6MM1xTNOLzWZDUcoQYgmSqasA
BlGUDkyzDtl3Ygy4EsuyMIw8ui4oFNzk80c4ffp/Yhj9gJNCQUEyhDGkY6ACPcBRpD6GkPkSo8hE
ThPo56zuDiGZymjx2JuRef82JNDoQQKRPFCHYUzDMB4G7FhWI6Z5JXZ7LdnsdtLpH6MoSTTtYxjG
QoR4Hk0rRdNWUij0outOMpnTWJYHXc+jqhuxrBdQ1ctQlABeb4DGxquw2Ww0NPgIhWbx1399JzU1
NcUOwJsuCGO/tj19Fm00xZJUH1fb08x7aBz+8i8gkwFdh8sug7VrYcUK+TNlCijK5P3/+PLlOEJy
SNrFeum8U+WtDot8E/h5EWScKUV1Az8HUBTlK0CNkHWJZ0IhPwc+D+xXFOUM65ERsgzgkpwnr1XW
ev60vVcDI/v2beCLX/w0w8NDdHW1Y7c76OzcR6Hwv1i69AFisU4SiUHKyoLs3/8LenrGsKw8lpVD
0yqx271UVX2SaPQhVHUTlnWEQqEa6QHVAX1IQzOMNF5JZBLXIaTHU4VsBfwMZ8HHPqRRsRWPiSLZ
jWuR3sz3iue7A5iGBB2PkM8PEI3uLe4r2RNFqcWyAmSzNjRNQdOmoSh9RCLrqCq7jwX2g6wtPMnt
PE8Vafqp5nfOD7JBDdHqOs7SGXbUNhcNDR+e7AK6bt0motEIwWBo0nMBO9XVdlwuDct6nmzWoKSk
m3x+DKfTic22hbvvXvhHNcN5t3btuyRvXNav38CGDd1EIiqnT7soFGZy5MgRJia+xM03fx0460hE
o1HSaRW3u55cziSfT6HrTiwrhBBeVDVBf/+TGEYYRbkPTZuJYZxAhhdnIMQWJOMQQuZCNQJOLKud
QmEnQgRRlASmOYppLgDWIEQYySouQzoKS4FSJIPxHFInlyBZx8eRuVUdgB9FmYXTuRZVXcDExFeQ
Cd4CaQ+04nlPIZeqVPH8c4CZqOpyLOsoQmwnnb4ey6oBdgAVqOpMTNNC02ZgWbLluBAZoAvLCgA+
TLMERVmOzzdIKNTHxAR4vX7sdi/h8OEiO7CQ5cuXA1w0jP1ye+rzzWBiIkOJu4Ep1OL96a+5o9LF
/S0taH198mbW1sLKlfClL8nXyy6D17ABb2YI/e2UtxRcCCHWK4pSBvwLkqs+BNwohBgt7lKF5LTP
yF8gn6jvFn/OyC+Q5auX5Dx5pbLWSKSNwcGjfOc72clpe4sXV9HYWEckkmPmzAvBSHe3wd/8zd+z
Y0eebPaySdpxbOwQp059koYGL05ngvHxGZjmGjIZHzBGofCf5POHsKxVuN1V5HLXYZovIsSzSEMz
GwkkVM4yD9niq4k0JhGk4dA4a2CGkPkUM5Bhjz3IEArF/aJIyrW2uK8dyXCsQhrLzuLxDmTuRhnS
oE1gmk4yyVpusE3wkfRvuXX4R5RZOXpw8Vutim3eG2kuVJPNdwK96OYIe/aYlJR4MYznsdu9DA72
kEjk+epXf0Fl5TLmzr2P4eEsAwOnGRsbRVV3MnfuTSxevBYhDPr7n2TJEp3PfOaBVx0V/2ryh+bX
XJJ3p5xZvJJJB0NDFkLcjd+/nFzuMJ2dP+WFF77OkiX3MzrK5MJTWmrD70+TTifJZNLkcjYsqxNd
T2CzORGihULBC9gwjC7k4i+Q+mMhQcAVwLeBDUigMYYQARyO5UA3udwwqroaTRvDskYRwo3sVzGC
DHcC+JFhylGk7i9Dhl9eLO5nYbdfga7fiGH8DqnPlcXj+4r75ZCORA7pZPQCvwPSKMooljUORDDN
3ajqdDTtMhRlDE1rQ1UvQ4g6cjk/lvUMQtQhwzQ2NO0wuj4fTVuA01mNELsoLe2ntDROf/+P0PUs
a9bMvoAdOD+MHY1E0AajNAxupH7gMAuSJ5ibbcchCuRVDXPJYrS77pJAYsUKuEijwdcrb2XPo7dC
3vKETiHE95Du5cX+9snz3r/+3qqXBHjlstYDB74FVOLxfAy3u4YDB3bw9NObCYUixcmlT7Nq1W3Y
bDZAgpPe3pO0tvaQyz2ApETLgLUoSpJUqpv+/nZyuSFMM4yiuAEN02xHiAyFwj5OnCilpGQaicQ+
8vkjWJYJdCM9oRKkodkEXAesQCaR7UEamhzSoFhIr0ZDGqVSpMfSg/SCZiIf2+rivkkk1QqSwWhE
ekmHi583gMzfqAGmoYohrhU/4y5Ocod4mIpcgiG7n8fcNeyqrGMfEBtXUdUcihXB5bqBQqGAzfYi
qVQv+XyBcHg9druLadO+jN/vIxweprd3Pv397eTzZdjty/B4GjCMdXR1nSQe34PP58Rm89PTM5Wv
fW3dKwKC12Ik3mh+zSV5d0tnZyc9PSOMjHjx+e4hnQ5hmjZMczrZ7EIOHXqaoaEeamrGcblchEIh
Vq+ezc6d24lGo5hmHaY5gqyA6iYYrELXp5DJHMKydiKBQ6H42oJMtHQgkykbUZRGhJiNBP9xLKsZ
CfDTWNbBoo5HkCxFK3Lx/h0SqIwWX1PI3Kr9xXP3IXWzAtNMMDHxFSzrNBJYzEGGTLzIEtUPcLa6
ZClSv38IJDDNbPGYmYDAsl7CskwcjoXk81vx+TwkEgJwFithnkdOX52FyzWViorbiMfjJJM9aFo/
H//4StxuN3v2dGAYLvbu7SKV+h733XcPLpdL6qXLRej0aZkrsWcP05ub+f6wTCEcsNdx3L+Kp8s+
SrORIzWjnUee+C6udxEgeDPlHVstcklev5xfyqTraXw+lZkzPzVZEjo8XIXL9QkMYzvl5TptbVso
FArMm7eCfH6EcHgr7e0tZDJTkQahG7gLyQTYUNXpOBwLSSaHyefDwE+wLDvSI/lr4EUymV2k048D
o+j6AiQ4sTiTByGlC2mIOpHlbTngz5EhjWFkes4I0siEkUbpJaRBcwAfRwKUNJIFKUd2+VuFNGIb
OdtW2AHUopPkOn7FXfyYOwhTRo5uyvi1PpOmUj/T7v4BqYlhjPSjbPhfn2HLlqf44Q+fxuW6nYkJ
Dbu9A8uahqbdhmnmEGKQdPoEyeRRHI65mKYHy5qHYQzi9y9F14OkUjbASSAwi4GBp3A4VObMWUB9
/ScviJODZCR++tNfsHNnG4bhJBRyXABA/pD8mkvy7pQzDFVTUyvMBsn9AAAgAElEQVQnTpxgfLyO
yko/Pp+DwcF+CoUMijIFRZlNOl1HMtlHU5PskisElJZajI/vJ5c7CmTRtCGEcJFMzqGiYjY+X5RY
rBUhPoIE/s8AZ8KIBSShfCVCdCEX5TYgimnWIoSKXNCvRuqtDalzW5BgIIB0TlqQoP42pG7vQOr/
Ks5UgxlGDplr5UaWvn4O6UQ8i3QcskhddiKBj5OzTbguR1ahlCCByMPAbnK5+1GUPeRy/4FlCSQj
qhav04eiXA/MIRSqpqysguHhvSxeXEtJSQlNTXFCoY8zONjK8WOtdDz1NKPf/hGrFFiUSVIyHgZh
IdxurMsv59DCRTyYdbMzt4iE+xZKS+bg8zkZH3+cBtV48x6Id6FcAhfvATk/JheLxfiP/3gCRQkS
iUTo64vi8czF6XQSjz/PnDkfZGzsGxw9+m16eh7B4zFwu8eIxRqQLIMXCQxCyHBDGYXCNoaGdmOa
qeKnHkUu3vcijckihEiiqq0oioppLkTSnP8PMvq1pXjOVcAvkb0snMD7kKGRAaSBuRnp/RSQoY0K
YD7SQChI45RGGpMjSINkRxqzUiQo+T463VyPnbvIcQfjhMjTiYOHqOMx5nOAElSRp8qep97IYbN5
MQwXTqeTO++8jX37Iuj6Sg4e7CQet7DbbwFqSaV2oSjSoxsbew6/346iFLDZchQKDjTNh93uJZkc
IJfLU15+LZbVi9u9mqGhQfz+JpYskYDi5V1NP//5v+eZZybQ9avxeCqJRrMMD7fzcgDyRtrGX5J3
nryRPJmzDNX9zJ5dzZ49TzM8fJCysmUIEcOyxrDZIuh6nkWLVlFb66G5eROrVnWwf38Pixf/dyxr
mHw+gMtVSyYzRHf3D9H1VaRSzRiGhqrWY1nNCHEACSY+hgw96Egw0YWi3I4QfUjgPgshZhYTs5ch
9bUGyR70I0HCgeL2M5UftUggcSUSBPwImVdVgdRbUfzbXs7mVfwZMhfru8ikbS8y5HIa6XicKRe/
EelcmMXPuAVpV/YA4+TzjajqAuBaNE3FNB9GJp7uJZvNYxglZLMnEeJFZs2q49AL7VxtzKOs+RvU
9B1hSTZMyJD9G7v0SroqL2P/gst5SU+w+P5lCE1j3boTdAZvR0FA/BDh8DYKBTvz51872bkXeFfl
SrxZcglcvAfk5Uarrq6O7dubOHbsKKb5LHZ7LfF4gvr6ZaRSbVhWlu7u3ZjmAoLBlSxePItsNklz
868QQkd6InuRC/swklloAg5hmnOBq5AGY1dx+++RIQoTXb8dRfFjmr9GiCEkeChB0qAuJMioQip/
GGmAZiBBw5l8i0qkwQkhPZe24jVdjqRVX0D2uThR/O+7kMBkITYCrOE4d9HN7cQIkucUIX5EA49i
4yAu5CMfA65FUXYTj59m69Z/x24vQ9O62L69idtuu4VQyEE+n8Nmy1AoFHA4GnE40hiGRi43gRAl
CJGhrs6GYdSTTDahKBWY5hCZTBf5/NPYbDMRAhRFIRS6HtOM0Ne3gVmzIucAgt/+9lGefnoAt/tv
CAZXks3GGR7uAKC5+egkI/FOaRt/Sd6YvNE8mfMZqmBwJpHIKTo6nmBw8CSWFUDT0qjqUWpqPFx2
2RWYZp7eXjh9+nTxMyqwrAyh0Ap03Ql4URSdXK6JdPoIUIJlva8IHLxIvb4W6TSkkEB9OzZbBtMc
wTSvQNNuAJ7ANF1IfTyCZDh7kc7AdCSbEUGyBHmkfXgIWfUVKp7XhXQ0piB1vbr4uUNIxsKBBCBO
JHO5EAkiUihKC0J0FN/LKhW5vxsZMnEAJ9D1Umy2e8lkYkAGy6rHspYDjwFZTOMw3oHHWTlxjKv1
Ma74gcmUZAQNSKl2jnmWsqlqLU8n+9jLHTjrVuJwdLNmxXLSyVM8s+NhwKKm5sOEw0lMcyah0J2k
0/vRtF1UVMxGUU6zfXvTq5YNv5flErh4F8vFjJYQo4TDtdTUrKK/fwjDaCCRyHPixC+BLtxui3D4
KHb7jdhsgq4unXA4x8TElUjPowq56B9G5tHWIUFGCLgJyQxkkMYIpFFYBOzBsrajKFOxrH4kDQnw
n0gDUopM5gLpeVQjQcxpzpaVuornHkGWrHYgPaE40jNqK17L+4DrgXFswA1s4C5+yu30Ukqadlx8
n1t4jD/jEL9HekjXIj0pE2nwvolp6hQKK4jHVxAMTqGuLkdTUyewmRkzfDz//FOUltbT3z9GMtmM
qnoJhUpIpzMUCu2UlanMn7+AsbEo+fxT2O2HyWZb0LQgmubE4ZiNZT2H31+Baeo4nY3E45DJRDGM
DF6v/DZ27jyGzdZIMLgUXXfi9crufbHYOJFIbpKReKe1jb8kr0/eaJ7M+QyVzebi5pu/TibzaU6d
2oQQtVhWBVDL6Kjg8OH11NVdhtcLU6ZMwettJp8fQVUNxsfDBAI1WNYgqhoml3NhmiuR+RFDyJBl
BgnW9yNBwWWAG0WxsNlG8furGRsbxjR/j2QjM0jHYhoSUNiR+qkXf/cgHYAhpE6PIEMWKhIMTCAZ
0ori+04kODCLx/yg+Bkni/tsQ4IMUNV5mKa7eI4uJMNRQIKcZmAYRVkEJMjnHQhhQ1ESeMxWruQ4
KzjFCpKsIENwxARgsGQqvfXL+Hl0jBetRXToJg1Tv0w+P8KpiYew2eYR8gRJp7vJZDIEAo309+cx
jCyqahCPR4lGD2K3N+D3T0VRtjMwsInGxjRNTf4L7nsq9Qs+8IE173km4xK4eBfL+UYrHG7luee+
ydSp17Fq1Qc5dmwDfX3NQBupVDtlZddQVvYhTp9+hGQyhctlUFp6BaZpomkKlrUbOZTWgTQIp5Bx
0yAyNNGINAAxZCikErlQOwAvlvUS8CiSYrWQSZheZFx0ARIcbETmUNQiAcXjSAO1FunJHEEyFi8h
AUkp0nh4kd5PC3Zm8n5auYvt3MYRSkjThp/vspRHqeIwceBfkSDmDM0652Wf60cCmgCmuZpCQWfa
tBCXX34Z+/b9ngcf/DmzZ89kYqIPVT1BMDjA2NgPcbvfh883i4YGQTJ5Er9/lFTqUaqrO/B6Xcya
9QBDQ6309XUwPNyO0xlj4cIbMc2ZnDrVQTpdwG7PkUoNEY/v5rbbZMWIYbhwu/WXjbUHpzNAOBxG
17PnMBJvRdv4S/LWyR+SJxMMBtH1ND09O6mvX4XbHaJQSDM+ruFw3IzPN4NsthRdX0A6fYyWlvVY
Vid33z2bmTNnsnx5I9///i8ZHq4nleordtJswbIGEeLPsNmymGYQy9qD1LkVSP2OA3tR1RxChLDZ
nFRU2IhE2pDAII9c7ONI5jJU3DaKLBk/09zuGFJnb0Yu/gqSMdha3N6KBDAqEpTsQup5Gpm02Yu0
QzYkUBlAggkXlnWmN0YjsppERer0KeApoApEBbMKL7KCX7OSOCtEF3MZRkUQxc4epvNfSoiX9ALh
xiVcd8e/kslE6exs4tSxkyTio8Tjx9G0EiwrjssVwTQrsdtlCDoeP0VpqZ3Ozl4GBzsIBt+PzTbM
+Pgw4fAx/P5DrFlzG21t41RW3nzBrKYHH/w5zz7bRSjkfk8zGZfAxbtUOjo62LJlD4HAXZMPr9db
jc3WSCzmpFAQLFlyH/X1faRSm4lGJwiFChQKW9D1XgxjbnEk+QRCaGhalEIhhmQqBouvGhJMRJA5
Dc8imY0zI2OeRBqUa5GLeCWSaTiJNAalyLDHmfwIW/F9O5K5AMkm6MhwRycy/qojjdECJLAZxEEv
7yfOXZziQzxPCSlO0MB/cQ+PUcURnkcaORNJpzYjDZOOBDuZ4nVXIYGRG7e7BJttBYpyjLlzZ9PW
1jE5S6Wy8uPU1Oj09j7GAw8sxm630dLSj2FEi8mWV7F06SKGh4epqvowBw4cprm5BUWBhoZKslmD
RKKB6uqFuN01pFI7OH16M35/CpvNMQkI0uk0oZCbWMzB0JBkJJzORqLRAxjGLlavXnHO4vNurXn/
v1XeaJ5MJpNh8+Zt9PYOcOrUr/D5tjNt2iI0zU0iEaa09INUVS0kHh8jlerBMLKkUr0sWzZjEmDm
cnkikUPkciexLI1MJkYuN4JlVeF01pHNPodlrUU6BvM4yzzMRc7zWAcUMAyD3t40pnkVEpxPIIFA
CqlP25F6e8ZGOJC6PYa0CVcgda0EGUY5VnxtLX72meZ305CgZQuSzUwWtxeK52xEJnV6EWIW0vb8
GYryFEI8RxCLKxlkJSdZgcZydhDAwqSPI0xlF1fwVTT2oNHBGgTzcbtOo6pRxNAW0r//V1TVj64b
lJSkSKfbGBv7DiUl19PYWEk8/hSRSA/z5s0kmTxFOLyVNWum0Nt7CkVpR1WXUlk5A4/HYGxsgMbG
EpYuXcwLLzzJtGm+yXv78llNodC9aJr+nq70ugQu3mVyJhSyZctL7NkzSEnJNmKxPubPvxOXK4jD
oRGL9RCLxYo98N1Ylp3a2vlcfbVsFXLw4OO89NI+UqkJBgcLZDIdmOZuNM2FaQpkqej7kAq+EWk4
OpEL9m1I5X8CmUvxEaSx8SOTvFYjZwb0IEFFGRKA1HF2hkAd0uDUIsHGFUhv5TCSFp0N6Dgo40YE
dxHnQ6zDj8VxnHyblTzKpzjG7UiG5UfI3JD3I0M0u5E06tTitZ1AAh0vEqzsBLIoigPLGsDn85DN
ZunrixYnqbpwOMoJhWQLlt7eDXzlK3/BAw/IxcDlctHU9DwPPvj4ObHUL37x02QyGYLB4MtGz///
7J13fFxnlfe/z713+ox6t2XJluWm2I5L4paK00lICCQkwC5Z2ktZwrKwDXZfdpfdBV5YwmcpW4BA
KAmQ3quT2I5rXOJuuajL6mWk0bRbnvePM2M5wYEUDBvH5/PRR9KdO/c+0p1znt/5nXYfPT3Q2Ajv
fe9yLrhgFTU1Ncc3lFAoxKpVjfT1tQIwPHwXfX1JbLudSy+dwoc//KGTfg7eajXvb1d5vXkyeTay
sfEviUTStLQcZPfu9ZSWtmMYPSSTz9PRcQClPILBGoLBMmxbcd55K0gmk7zwwgv86Ee/ROtzqK+/
HtOMkskM0t9/J0NDWxBAMIxSGbTOj0DP95CQyhIJN0TwvGIEcJyN6HYZAgS+jjCTMxHmYwmShP1D
BDSEkXBIFAH42dz3GYhu1yBsRL7EtQgJa5yHNLwjt442RKcbkRDpPkwOMp8RVvBtVhkBzvV20phr
m9SPyWZifI0yNjOfF7mACYYR8LMHmIFSy/D7DAKBcjKZCTIZk2x2BZWVl5FOtxOP/5KGhmouv3wO
ra2HSadNurv3Ydv70Lqe4WGL1atnc8EFq1i7tpNIpJ7e3vuIx8Hvh7POamR4uI3vfe9+9u/v48iR
bzF79nKmT7/ipLOa4PSt9Drl4EIp9WngC4jLuAv4jNb6xd9y/kXAvyM8XQfwr1rrO071Ot8qkjc+
BQU3UVw8QDYbobl5K677S0zTz/DwPuLxVtau9dHY2ERJicJx1lNSMpvSUqHhI5EiBP1nMM1RLKuT
bLYL6Xe2AvEipiEeQxfCRlQjj+MbCH1Znntd4pvys4EYiiACMu7OnTsLMT6DuXOLkI/e1YiRKkcM
UjlBHuVyjnADzVzDZgqw2UuYf6eAe4ixnxokh2MbwkisRUDJMuBDiIdjIrX2jyDeVhYJuzQhoOM+
IJiL3T5EOLyUZHKYrq6XSKfbiMWibNx4lNraERoaaujpEVDR2Ch5DXfc8YtXiaGvfZkH8loZhslQ
x2GGhlwsy+OCC67gwx/+0GlJl55O8rsqQF5PnswrQyhTpkBT0yI6Oxtpafkafv8cstlFuO4ystlB
BgfvRuudhMNJvvSlbzE2ZjM+7qevb4xAYB+BwEIqK28iFgvhuj4GBp5A61EMowKlpuO6TyBs3wok
dAHCHIQQwL8VMdvTEAYigACCeiQ/YwcCOuoQ21CEhDU2MTk+yo/ofA+il4VIvtR9iA7nGc1KJMwy
jOjwADCFCnwsZwsraGU5BziHdiJ42Ch2eyW8EF7Iv2baWOdMoZUrc+s9iOR3DSEh2QEmZxAdIhic
i89nkU4Po1SIQGBO7m+rROtZBIPt3Hrrp0ilUtx556+wrNkcOtTDwYMHKSkJEomEgQ1Eo1Bauoym
pinHJ0Rv2/Y/DAwUMW/eh5gzx2H//sPs3r2P0dF+xsYKfmNWk99fTkvLGEePHj0DLl6PKKXehwCF
jzPZ/vtJpdSsk006VUrVIzvC95G6qEuAHyqljmmtnz6Va30ryCuNz+jobpqbx1DqXHbt+i+Uqsbn
ew8zZ3Zj23vYvftpGhr8XHJJEf39Ln19u/H7Y3R07CMavRalgkSjMXy+epJJA633IcyChyi9RlC/
QliI2YgX04YYpOcQ5iDv0YwjjEUKMVAOYoTm585vQwzK9NxfNB3oJ0gzV7KTG9jA1awhhs0e/HyT
Ou5mPgc5ihifRYjX05u7zsPIR7gI+EuUKkVrF6VmofVl5EGErONB4C7E0JVRUPDXlJamGR7+NobR
QnPzWiYmWigoeAe1tZ/HtrM0Nx8mHj9EY+PLJx++nhj6a2EYzoQ63nryeipAXmuezMlCKOFwmIqK
WrZuNWlouI5Dh0ySSRm+p/U0lGoGZrF/v43rnks0ugTD6MW2t3Hs2FNonaG4eDXZ7ARKVeLzLcm1
7v4Bokf5aqwIsrEfQkBAEGEXxhBWcgRhONqRjbgUYToeQQC+h+jmZQjDuQVxKPK5HGtz9yhGnJBz
ERDRkTtvPj6u4Wx6WM6jLKeTFWxnOgLKjhFjE2V8mTo2Y7GDGCmtCDh9ZBwTeA+yXTx9wpo3kQcN
su5utE6TSvURCFhovY2qqqkEAkPE40P4/TBvXiPR6BGGh4fZuHErmzc7jIwsZ2wsSjAYYGxsA21t
JqOjcUpLR+nrexy4ksJCyXlradnC9OkfpL5+GVOm2Ph8MZqbXdrb78GyXKZOvZimpuuxbZt9+w7Q
3Pwitn2I7373HlavPnxa5V+caubic8B/a61/CqCU+gQykebDwP87yfmfBFq01n+d+71ZKXVe7jpv
e3Bx9OhRenrGmTGjnGRyiOpqi0QiTXv7AENDPVRVLWT+/OU0Nc3Ftsfo7NyIz7eeL3/51tzQnfto
aRkik+miquocenq209l5DNdNIQYggSRdZRCUX4kwHK2I4ViOUKCjCIXZhxiRBQhF2oKEHBoQAzUd
8RruRZKvQogHs5gQ7VzJT7mBnVzNGqKk2UU1X6eCe1A0Y+fOb0WYh4UIuDERwxHOrbMACbOkMYwJ
PC+G1jbCkgwipXH5ctjdSFjEwfO+SSSyiIqKxVjWIYJBm0WLLmFwMIptdxIM1pFM2rS1PcJ73zuZ
93Aqe02cCXW8deT1VIC8VvD4aiGU/v69gJ+zzlpFT8+LaG2TSqXw+8/Fslpw3U6y2fMxzfNIJIKY
ZgzbjpJOf5vOzvsZHGwmk2nBMFKEQqWMj7cgeVX59tx3InqlkY3eRexADwLi5yAAZAeixwlk66hA
QMUwoo9tSPjUjzAUTyN5WRkm2c0dSIijhyk8x3ImWE6GFTzKEn5IEJsMFtup5n7K2MxH2YRDFz4E
kHQi9qcHGMOyxslkOhGmZR1ix25CdP5hhCx/CmFb0sBGbHuITMakosJi5cqPUlt7LqlUilAoxPj4
EVxXtsUNGw5TUHAl7e0pCgrmEo1WkkiUEo/fR13dO3DdcVavLmTXLgGNrjtEVVURixdfRDKZJJVK
MWvWTOrqymlp2cfixUXs2WMwPHyYjo5x9u8/jFJHmTv3WiKRZadd/sUpAxdKKR+yE/1b/pjWWiul
nkHc2JPJcqRV3InyJHDbKVnkW0RO7Na3d+8Btm//MoZhYdtg21k8z8bzElRVeTQ1NeLz+fD5Sqmr
u4COju0cO3aMuXMbqampAOAf//EHNDdvwLYrkISuYqT3xEuIgckihuJqRDkjiLJGmWxw1YHgxO8j
j+xJhN6cixiBnyGMxlSEyfARRnMVCW7gP3knQ0RweYlavsql3E0FhzmC5EdUIZ5TAAE1acTAFSFG
rAMBNLsRtiSEUuvROp2bH3AQMYIjueup3N9wA4ZxIdCKbT9HS8szQDGe52GavUyfHmH69OX09eVj
qBkKChJccEG+7Pb1x9DPyOknb7RT6u8Cj68WQhkbe5GaGj/7928ikbBQKoZSDn5/H57Xi+NYaD0T
n28WnpdCqTiwFc8rxXWXonUTgcB+HCdJIvEEhlGF530a0fnlCMiwEF3KA3MQPW5FmllVIUCijMk+
FG2IrbgZAf4HEaAyiDgDKnfsIAFsFrObFexiOVmWM05trq13GyE2M5Nfs5rNnMVLVJGlFcnfyE9A
vp7JCcr57r13Y9tliFPTgtiFGxCbdoR8C3NhV6/Fspbj83WRTv+YVGojPt80nn76W5x11g6WLPko
/f1HOHbsYa69VuZ/5PuFZLPtFBYW5p6zlJP7fFESCYvLLlvNTTeVHG+W9dWv3sGOHc8zNlZGNit5
GAUFg0yfHuZjH/swa9asZc2aO2luPkQoNIVZs2TqtM8X+p2fn7eanErmoozJsoITpQ/5JJ5Mql7l
/AKlVEBrnfn9LvGtISd264tGb6O7exTXvRytZ2IYHWj9IEr52bWri5GRr3PFFX+JZVm0te2gs3MP
n/jEWnp6svh8BdTWRujpaSORKMZ134Hr+sgncAlxlG+724MkSkYR45MHFI0IGHkCwYhNCEX6EGJM
JhDvxAbOIkI7V9HBDTzCVaSI4LGDEv6FWdyDyxGiyMfkxdx9z8ldLw9KDiJhDQsxbuHcWvsxzRCG
UYbWATzPwPPuzv3HRnLX/CICfLrw+/8Eyyogm41iWUvRejOp1DRM82YCgRpMs4uWlsfx+XZzySX/
TCo1TCLRg88XoKam5vizONNr4oycSvbqZCGUG2+czdq1fTz22LNofSWWNRuldpBMPoBhtKLUQpQa
wnVHMYwCQiEftt2GaS4hGCwlEhlCqVoSiVW47oOISS1BWIZBROfy+VX7EfAwgOQxTUXGpefLUV0E
kMSQ0Ol8RN92Io7JImA39fyQ5cByRllBirPJ4EeTxGAb9dzJQjYzzmY0vUQRwFCD2BMLCWnmp6rm
Bx7W5u4xiNiXIbLZMYStuB/ZckoQ29WC2KJaII7PtwAoJZuNoPW7gF6Ki/8PIyNd7N27kc7O9+Hz
xSgqCrJ9uwbWEAw6jI0dxvP6SSRaKSqaSzrdjt8Ptp047kycCBpNc4Tm5scoKvoTCgrmMTa2n56e
x5g5M8TUqVP50Ic+wNy5WxkZ+RkzZvwlxcX5EPHp12n3tKkW+dznPnccXebl5ptv5uabb/4jrej3
Iy8f6TuFeDyNaZ6D68aAMTyvAMNYhlJx0ukaDh3aSVfXbQSDE6TT+0gmN+N5MzGMqSjl0d8/jOd5
ueYyacSItCPexwZkA78JMSKHEAagF2EkOhAjcy5COX4bUewQAjSuB14iwgauppUb6ORKWgnjsJ0i
vkIV9zCDo7wfwZeHkKTPPMV6EwJeBhDDVYEYh725dcxHAMxRYCeGMUEwuAilqkgm9+B5LYiBWokk
kc5AKNz7sawqbLsX1z2A1lFcdxS4GKVmY1k+yssb6O01aWn5AaOj7ZimdbwXxSsV/XTpNXHXXXdx
1113vexYPB7/I63mjckfQ+9PJXt1shAKwNq1+5k3L0pLywsMDT0HdOJ5Q7huFGEXEmQyHkotxXGa
cd1+CguLqakpJJstJZksAqowjMO5IWGbgY8gYY91iJ50IfpViQB9gD9DwMRehEnIIgBkFAl/FBHG
ZCkpVrCX5WxiOe1U5ViJw0TZzCzuYAGbiLCHURzOyl27G7ElGQQIHECAw0juPjcibOV2xMHIN+rK
sxUu4kREcudUI4nc+fX7EPtkYZqlZLMpYALLmoJhFBGLTaew8CI6Oz0SicdZuvRmZs58B9nsAE89
9RDx+Fba2vaSTJaQyTxHJFJFOGwxbVrwpLZhaGgI1y1izpypxONrmZhYSygEVVWNuG6CoSFhJBoa
GqiuLiWbHedE+UOwn39InT+V4GIQefqVrzheyWQq8Sul91XOH/tdrMVtt93G4sWL38g6/1fIq2Wd
n+glDQ01k0hkiUSuQGsT2zbw+UrwvHoc51mCwSDpdBvj490kkyE8rweta4BrcN0hoAvHUQgj0IbP
N4hUc2SQoULPIklRec8ghFCMbYgCp5H8CTf3vs7c8fOJMoOreYwb2MCV7CSEw4tU8I+s4F7eSwsL
kYztXyDd/eYhYOExBLRchzTdmYoYhiAS9y1FQMYQQrlWIkajlEDgptwkxAO59XjArShlARmUmsDz
hAHJZNYACwkECvG8Dlw3CxRhWQY+X4jCwgJcdx79/S6HD99GY2PDbwCGE5/R6ZCAebJNeMeOHSxZ
suSPtKLXL38Mvf9DsFcnesOHDx8mnfZx7rmfYuHCFE8++Q06O+tw3ZtxnGFEVx4CfgU8huPEgRGK
ikbx+2fg8zUwMpJE62ZEd1YhG/kvEZ3WTFZp/ClwIcL4vYQwCSlE76YCHczEZQUhltPNcr7JArqx
8BgnyFZq+SHlbKaYLRQzyA0IgJiC5HnsRByTfPLnDKR3RgphT9Yg+n8Vk5VoBUg9wDQEQDyBODnL
kPki65Dw7aHctVYiDGci93sZjtOFUj6UsjGMQwSDIUKhBrJZi/HxGIZRwuHDmt7eZmprS4jHobW1
itraKxkbi9DXd5Tx8ecJhfqor1/NhRfOO2lCbv45TUz0MzraRlFRPZFIBR0dt/2v6LT7h9T5UwYu
tNa2Umo7sBr55KOUUrnf/+NV3rYJ2WFOlMtyx09L+V1Z5yd6SVoDZFFqHNctwvOCOI7CdXtQygFa
UWo2pnk1wWAticSTCAV6CFHmDyKPfD2wFcd5Bsu6Gsd5DDEsxUg1SClifGKI8h9FqNMjiLcyE8nf
HuMaNDfwPFfwXwSx2cpZ/F/ezT0coY3piPexADEeVYhh22YPxjIAACAASURBVIh4IQZi1CyEGcmH
SMqRErdfI4bGQwxMBKXehdYRoAulFKY5E9v+KYbRn1vvNrROo1QWz/MQr64brXdiGE34/bWYpo1t
92EYaSCEYWgCgQDB4ADV1QG++MU/ZfHixceV/Lc9o7ciqDgjb17eDHv1egaYwcuZklhsCqFQjKlT
38OxYwbZ7GFctxilPoNlPY5p1uB5a6msLCaT2cHISAzPK2F09CCuuwlhAhcgm3UU+AQCGu5CQpPb
EcdiGNhDjJ9yLj0sx2MFCZbTQyn7ADhAIZuo5r/4CJuYxn7m47EeqQwpZnIo2YnzRBYj7MJw7v4P
IEAhlLvvAKLH9bmf7dzPuxHnpwKxadMRmzaU+zkGTODzVeE4e9D6KEr1UVSUxXFMtH4GxynHcUaw
rBYqKi7B5yulrW0X2WwvkUgRodAiMhmL3bsPkMm0YFnLmDv3AoqLi0mlVjE4uATPu5+/+7tbaGxs
POlzCgZttm79PvF4JpdzsYHCwgD19fbbrtPuqQ6LfAv4SQ5k5EtRw8BPAJRSXwVqtNb5TkH/BXxa
KfV14HYEiLwXgbGnpfyurPMTUW5h4QoiEZOBgV/huiuBWlx3DHgIrQdJp9MYxi0EAisxzQlEKacj
/8pzEGXOMjn59GFc95eIElciinoIMUAOAiJGmVTwuRRwN9eQ4AbWcTkHCaLZzBS+xKe5l+W0H4/F
7s29bz5iXCYQzyWIsAy/zr3en/tP9COehg/5iBxDGJTR3FrKgUK09ufON9FaYRhFBAJFhMN+TNPH
4ODDeN4StL4OAUIvYFlxwuEBXHcLExMvEAqZRKM+kskXyGaDBAILGRl5gdHRn/HOd87g0ksvfV3P
6Iy8/eSNlA+/3gFmeTnRBgwNzaKzs4eJiQSZzDDBoELrBIYRxHE6CIVSBIMhVq36NPv3f4u2th+T
SDyP54FlLUWpK7DtRxHQ/jGEVXgAKEDx58xhDyvoZTnPs5wemujGAEYIsIVpfIcmNvEBtjKLUQ4i
XTfjyMa/ncl+GAmE4Rwj32VXtpsuxBZohAUNI10H5iFOxyhih/KDzdpyx/L5HpHcVykCKGYiNmMC
eBbLcolEFqDUERYunE8w6LBhwwFSqX48Lz+0sBq//08ZGNjH4OATaL2BVKqaw4d3YZoejvMc2Wwb
0egqtm49wPTpFTQ1zSUSWUhHx7O/9TmZ5igHD/a8IufiZzQ0hN52nXZPKbjQWv9aSWemf0Z2r5eA
y7XOtVQTV7b2hPPblFLvRKpDbkU+iR/RWr+yguS0kFdmnSeTSSxrCgUFF7Fhw+PHs4YnUe6zlJc7
DAxsxDTbcZwgolRSlqW1H8+LYJrgOG3IppxPbqxGDEkv+dIxrSMoNYxswuUIu7AltzoTCZWMUUiU
d/EkN7CXy9hCAI9NVPBFariHuXSiESVvQryKFgTEHEMYkMbcWvJAIYQAjCTSUOcepI1wCWI0epFw
SQ/CWsxAPKDu3Lr8KGWi9Ti27aH1ONXVGRYt+lueffZ7jI9X4Xk9uO44llXJ1KmfYWTkNsrKljM2
VkQm00lZ2cUMD/+AbPbbeN40PM/lne+s4+tf/8rLnpG0Wd9GQcFNr6sy4Iy8PeT1lA+/GZB6443X
MzHxU/7pn/6ZgQED6TY5i2y2DqXiKNVLJFJFWdk7iET2kk4P43lJtB4DRlBqMVqvxDSHUWqb9L+g
lmU8wnLuYgU2y/g2hYzjodhLORsp4ltoNmPRzBI0BQiQKEXAwwjCJOxEdH2cfP6HbPwJJC/rQsSh
6Ub0vBWxOaOImV+M2J4w0pHzcSSR8+rcvX6NgJH3ANcgYZCXctdZhDgpI0AxSg0TDDZTU1OL1kNs
3BjBdT9DQcF8PK+LiYnHcJxt9Pd/CdcNAHGCwRKy2SI8r4hs9nm09vC8QpQqwOebT3PzYeAA1dX8
1pwIybkoZvbsixkbU0xMHCAUUlRWXoXrvnQ85+JEOZ3Lz095QqfW+vtIveLJXvuzkxxbh5SwvqXk
9VKdMJlPUV1dw9at22hvH8TzLAKBNMFgK8eOHaO0tPRlKHfTpk186Uvf4dChNjwvhNa1wFW5Esxf
odR+Mhkrl1vRiGz0JgIo9iIeQQ0SaRpC6zjCYhjILI9CoJNCuriWF7mBCS5jAD8uG6jhb5jKvcyg
i5VIAmgMYR1+gUS/UohRCSPhlB8gMdDpiPFpQbyUsxCiSmr4xUCN5NY2hrAWTQgAmUCqRkYR+rYc
8JNMjuD3D1NdXUJhoUd39yMUFzdRU3Mtx461MjqaxDBKOXYsjm07jI39D2LIGvD5jlJbO4N3vWsl
jY0NzJs3j3PPPff4s+nq6uIXv/gVmzYdYOfOEYqLBxgd3U1T01x8Pt9pl9l9Rk6t/K7y1ZUrDwO8
qv1IJpM8+eTTxON+/P75QALPK8C2FUr1k83eg20rbPtXxGLdtLU9jOPU43kXEYkMkxhdxxx3Cyvc
UZYzwHL6mcOFAAwQYjMr+X98iE14vEgTCSoRXatDmE0TMct3AD9GHIQxRD/DSN+bDwI/RwDI2UjV
2DDisBxA8ju6EVtTnfvdRfIlMojtOBuxBSaSQJpP9PwYYkPylSX5qrQ2BFw8C2hSqTYCgR1UVMxl
27ZRkskLMIwGQBMKLaCwsB7b/g/mztX4fAatre9kdHQGPl8Ptv08tv0ScBF+/wCetwnHmUEwWElz
8zpsu5sbb3z1nAjJubBYtuxSPM93vHeGYdh0dOx929mK06Za5I8lb5TqhHyMzuGxx35JT89UDGMa
fn8Uw9iHzzfKunUbmD9//vHzS0tLqaurI5MZJZPRwCwMoxTDqMbzFuK6L+F5m8lmHZRahlL9aP0S
QhrtRxTybAQMbEY29RUIQ5CiiEu4jm5uYA2XsBE/Di9QzF9xJfcyhW525d5ThhiJToSheC/CcuRL
Wk0ECBQhhqITMQggZNU7cvcMIGzKzYgB2p67RimTbbwNhL3QxGKXMD6+HhlgJPjTcVL09h5ibGwH
dXUZEokE8fg0stkqLMtD6yCeZ+F5jUAjSm1DqY0kk7V0dR3h2Wfn0NpqsnFjGwcOHOaaa67k4Ycf
58c/fowjR2zC4WI8zyWdtmhuHgMOcPbZC870tTgjr0terXw1HK5hw4ZW/v7v/wPTLP0N+3HiLKFn
nunFtsOY5hy0DiJNi0fRegcCNspJp+OkUja1AcUVxUuZNXyYxaNbWOIdIoqDg2IXJTxDgH9hLpu5
lqOMIc3mRhGH4RDCDPQjVV1XIY2o9iBOQQXCVIJUm+SbZm1BcqMuRByJAJLTEc5drwhhIDchoGUz
AlDORRjNPUheV4bJKckPIE236nPHDcQ+KKAbpR7K3bsGrV38/qMEAqtYv34vExMpYDGmuQzPm8C2
WwiHDbQuJJMZp6CgnNra+QwMxAmH30cgcAjHSeB59VRWXobnPYBt343WBra9m6VLl7F48YKTMhDw
8tyYysoFudlO0Na2Bdd9a1Vh/T7kDLh4k/JmqM7S0lIcp4f29r0EAh8nHK4jkznMxMRGpkypZ9eu
3uMf5FQqxe2338FPf/oQbW3laH02sBKlynGch9B6DKXeDXwGpcbxvE58PgfDKMe2b8mNU38ASX1J
Ixv+NIpZxnX8hBs4xCXciYnHC5zNF/gk91LMMZ5AolMBJrO7bSReWoywCDsQhb8MYSUSCIuxE4l6
ZZGEzXMQRqIZAScWkpNRjSRwbkHYjDBipGbnft4DJBkfX4NSEbR+D1CCUu143hRs28B1jzJ79p+T
zd7OsWPPU1HxMfr7XVKpETxvNzAD07wSwyjCMEZRqozx8VL27WsgGl1JJBLjwQef4YUX/oFjxyrp
63sH5eUXYJopEon/ZmzsDoqKPk5bWwdFRSnGxp4/09fijLxmebXy1R07nqe3N87cuR+hsnLhb9iP
vH3JZi/BcRrRWuO6nfj9TSh1LanUd7CYyWIjygVWhsXZ/Zyrm2lIjkNyO31GGZv0DP7N/AhbVAub
HEhxDqLPD+e+0gg74EP09ZLcsfmIrj7BZNvvmxCwPwcB/xUIWFiFMB1hJEF0AwIYsgi7WZH7Kkbs
RQHiaDyDhENnIuzkDgQs9CIh1mbE3uxAnJoXc2vrAxws6zwcZxpKtQNrcJxZpNMfI5Van1vXEwgD
WoznzWBi4hHC4WGqqsopKAhRVBSlrW2cRKIdCKJUmmBwhKKiEny+S1i5soG+vm10dx+itXWcr371
3ld1IF9ZBRIO17Bjh0xDrqxM8I1v/OK0HrH+SjkDLt6EvNFOffkQCsDEhJ9YLINS68lmt2JZUFY2
HcMI096+iaNHjxIOh7n11i/w5JNDjIxE8bx3o1QVWo/juim0vgh4AK0hHJ6Jz1dLItEE+CksrCSR
cEinG/C8/YCPEo7ybjQ3qpe4WD+GicN6CvkcH+Q+bqIHxcsVWyMZ5g0IcEgjsc48k3EEGVRmIhRq
AOnQ14MYmwGElTiGGJp8k5uzEDCSRjySeYiBGwQ+hWSIa6QeX0pTtd6LMDAhhImowHWH8TxFWdkc
5s79FP39f4thPIxSgwQC5aTTYZRqBI5gmtW47lS0BtO8GaUytLRkiUR8FBevYP36F5g37zosy0ck
UotlBamq+jDDw9/CMB5kZKSDVKqOa69delpldp+RUysnKz/s7T1IW9sjzJixjLq6C4DfDJWsWbOH
QOAqIhEp5TSMOqq8LCuzd7JMP8i5rGMpI4Q8h2zGYgcNPMJSNtHJvtjHaPMWkc7sA6bieb/GYyaw
HNOchesuQDbtJ5FycANxAPL6OB3R6XsRhiGIJFvm54NoJqeqRhFmYgABFgcQgPAcss3YyGDBfMv+
FQi4+CpiP4zcfW0EhOSryWK5NTyHsB4eSh3DMHZjGBE87xm0HkHrIaAJzzsf255A67m5az2B696J
9L0ZB54hEunl3e8W3X3wwfVMn95Ae3sPWk/ged0olWZ8PMK8eY04zghHjz4D+IhEPni8bPTVHMgT
q0A2bGiltzfOjBnLWLToz0gm+99WieBnwMWbkNfbqe+VIRTXjdPe3kVFxVmY5pX4/dUYRoihoafp
6nqCRGKC7373PrT+b9atG8DvvwGfby+2PRvTLMB18w2wyoBBlGqnouJyLKuAZPIgWleTyYwDXZSr
TVxnbON6L847mEChWKeL+Asu5T4q6GUHsqlvRoxHGjEkJmI0liKsRRcCElKI4s9F8iY6EC/FzK1n
Wu6vzuSuOy93bjWTyV8Z8olYYmg6kBhsEZN5IlciQGYEqZU/gORyRNG6DMOwMU1QyiGVGqGm5iwK
CupobFyCz7cPpa6jr6+MePwQhlEBjGIYfsRLKSEYHCEWm0lnZyuFhT5SKT+x2FT8/j7S6TjRaJBw
eCa23cisWbOwLJd/+ZdPnbQU7Yyckd8mryw/dN04lZUJFi16eepZYWEdra0O//M/P+LF9QdZ6JXQ
MLqXn9u7WKa7mcYQaOggwCZifJFr2en/CNvcZUy4I0jS5H9ipX6F665H6zCSB9EJLMEwpKxbwEMW
CXnkqzAKEPAeRADDuQgAqUBsQz4vKpR77xEkfLIVcRo6csfORZjMCOKQrEO6bpYgTsW03HkgTMUE
UIJpZnBdG+l7swTZovqQAWlPYpol+HzH8PsdSkpuQakeOjv7cZw6pMOwQzo9iNbtSCglipTe78qt
7wAf+MCHufHG6xkaGqK391ds376Ojo5dDA9nMM0wPl8rgcAPCQZXMTGhiMX6aGz869fkQObz41au
PMzf//1/MHfuR44Dx1is6lXfdzrKGXDxJuT1dup7ZQilt/cgQ0P/STDYieNswrKuZGTkeXp7m4Hl
zJ59NoYR4plnvo5tB6iqOo/x8WYMoxfPK0QeXxKpK28jEjmX8vKbGBrqAp6lyHmK946N8176uFCP
oYB1qopb9UzuxU//cYYiC1yMAIpHEVrTjxiC2YgHkcydV4kYnmYEIOxCQMd7EW+kA/GEXmRyeJgP
8TryLMXc3H/k3tx5FyGG69e5e0eREjcTSUoN5u4dQsIw+3LHM7juYQxjA9lsgk2bfkZlZQ3V1T7g
GJWVNXR1bcLnawIGcN0O4DCBwFSy2VYsazvFxcuIRiuJx1sZHx8mFMqi1Bi1tSW5LHFw3Q5cd4h0
+iA33rj8DLA4I29IXll+CPCNb/yCZLKfWKyK5MQEwf7D1LU9wtKj99D0xBj/Ot6HXz9IigDbqedu
tYiNuozN7OYYNrLR30DIXIbt+XPefDfQgePkpxEXIBtrBrgfrUfxPI1h1OJ5GtHtUiary2wEFNQh
joBGugJkEKBRnDsHpHw0iyRU7kf0expiN0oR4JHOrfPR3PEliINwN2ILPoTYCSc3Bn4/Sllo3Za7
h4lpXoPntWNZhwmFqlAqwOjo43jeBEpdf/zvU2ourgtSSbIJyc2oQ2xVCUoV4vf7+MUvfsnWre0k
EtDd3UYo1Mhll32AoqJ6stl+BgaeZNmyCBdddD7f/vZjlJa+fGLFa0noNs1SKisXvu73nS5yBly8
CXk9ndZOFkKpr19Ge3snLS0/Zdq0BCMjt9PXtx/Pu5j6+lrmz1+Mbdv4/ReSSj1JJtNPcfFc4vGn
cRwbravw+WT+hm1nMIxqJlq/xxXDT/MefZgLGQANzxHgz2niAT7GkLkYx9mBKF4BEusMMlmvPgNJ
phpAqNAEk53zTMQb6EPyIMYQluEcJrPHpyMsx3/krhdHPJX5CDXpIbHVAGKU/hMpO80gBu0mJFdj
O8KMtKJUJhcOCeXW8gTiCUWAcTwvhWnWYNurOXjwIa64oogLL5zN2rX7mZjYz9jYkwQCNplMHMdJ
YNtnE4tl8ft3Eg4vZmKiE8c5SibTzfnnT2No6HnKyy/BthUtLY+QSKynoSHBjTcuPxMKOSNvWo6X
HyaTXF/m0vvAX9MwMMyc0SOUOyMAdPiCdNdeyDcjFg/1B3lJX07G84NuRaktKJXBoAity/D5NqJ1
DM+rROuDSB5DMXALsBylRlFqN54XQprMrcayTDzvNpTqQ2sfsglHEXZjKqJ7A0ge1GyEjbwyd+0N
TDolHqLfDUii9iOInl5wwuse4hTsyf18O8JQukh+xwIEpFSi1DsxzU7mzw8RCs3gyJEOkkmFbe/H
cQaJRK5gypRbUKqA9vb7SCQ24Pcncd1KtH6CyQTwDYiDdB1in7qBx9C6kB/96GlqahazbNknKC+P
sXPnEOn0ErLZUmpqpgPTCYVCHDlyH+9+d/EbavV+ZsDhqZ2KWgx8FylW9hA39bNa64lXOd8C/hX5
BM9AdqVngL/VWvecqnW+WXmtndZeLYSyePFFpFIPU1MzSiAwTk9PhlisBihm7dodVFZGiUbrmZjQ
jI7eRyBwPpalcZx78LxhLEszr2QGl4y3c8X4P3O+TqExWG8u4LPGBdzrTdCvR/G864GrwEkgoYkP
Ip6EDwk3GMjwnyLEOBQiHksEASB9KLUOrR9FvJY8dTqUe0+exbByr7mIwWpCAEGGyWY4JUxOXvQj
mepLgTBKdRMKBdH6ENmsiet+C1iGUuFcvsQ2tC4Frs2trQOl1pHN7icUUkyZchXx+BoikQCf+MS1
PPdcCU8+2UkyaTI6mqS/v4Nkcoiionk0NjbR0fETxsd7aWjwc+ONV3HNNX/Oww8/zoYND1NYCOec
k+ass+bz/ve/j6lTp76pz8oZeRuL1nD0KGzeDJs2yfddu7jCdUlbFjvMIu6JNXCwsI5DJRXs6DpC
RC8la9TSbzyC6z6MsIZxYCqGMSPXdTZDKJTCsp7FdXuw7VYkn2kZMBfTLMMwojhOB3nWzzR34rot
aF2I5EYVIjZgB8I+7ESARjXCfFyNgIm9iHNxOeIQmIjT8A7EUYkh9uC53HXy/W2mIxUoZYjz0IGE
SFTuvi8irEMa04zg8wUJBHaxYMEFLF3axNGjO9i27WG0bqS6+qP4/VIOXl19DRMTNn7/MSorP87A
wHoc5yGy2Q4kfPrJ3Noj5MtXldrD2FgxhtFALDaTVKobyyqlqGgVnZ3dzJqVJBwOH2cYgDfUqvvM
gMNTy1zkB0GsRnaQnwD/jexqJ5MwUif5T0gmXzHi/j6IBPD+V8pr7bT2akg2mTzGggXT+au/+gA/
//ldNDcPEYtNo7h4Bel0nNbWw3jeURynn3R6G8PDO0inU0wxbG4pMrnZspnV/QRaGTxvRrlVreap
yAeJ+woZH+8j6/bheU8giu0himYh+E3lVjEz9/qDCGMQR0IYsxED8gQwG63nIAZGDJw8onwCZwAB
GQ5ChU7kfg/mvj+HDECqyr2+DfEmliG5FQkCgQhlZRFSqUM0NjYxNpbgyJF8SVwI0yzGdSeAK5DS
VxulxgiFGjDNHmbNMjl06GG2b9/L5s3dhMM2pjlCefmlxONRotEriUaL6ex8hL6+xygufoqlS2fT
1LScD3xgEjyc7p3zzsgfQMbHYetWARH5r8EcoJ49G5Yvh49/nNE5c/jbn60h415CNFoNQPfarzEy
MkJ//yYsawOuO4rP9yVc10LrJIHA+fj9R1BqguJii/7+PZhmCX5/EsuqJJWKIBt9F1qX4nkKraVh
lGVlMc3NZDJ9SFOqCJI/NRsx0z1IaKQXARggLGe+kmMmos9tCCgZQZyUEiTHohTR/TVMJnIeQsIm
lQibYSBgZRwx9Y3ALLQuwnF2oZRBTc04rnsfAwMQicSpqBhnYKCBnh4fWvdjmmJ7LasI295BONxN
VdVV9PRsYjLRvDR3j6IcQ2NjWcW5/1EJIyMjFBeX4PeD542SzUpeXDgcfhnD8EZbdb8dWnz/Njkl
4EIpNQeBt0u01jtzxz4DPKqU+oLW+jcGl2lpJXf5K67z58AWpdRUrXXXqVjr70t+V6e134VkS0pK
6OnxaGxcSU/PVtLpUoLBOpJJm8HBB4lEZlLvX8qqiU1c5e5nlXsMd0ixp+IsHrjqezweKOCZnXcT
CHyAgLWA0Hgvw8MWnrcMeBphDtqRzd1FQEIS8U7y0wNtxAMZRgBFvkwsjhiX5xFDtCD3nhWIh9KS
+yvTTA4P6gbejYRVLkeSzB5FMGR+pPtZCEDJAvejVJBk0kHrY9TWfoGGhkvZsOGbHDiwk0gkSjxu
kU4bKLUEyyrGcXZhGJWYZgGWtZFdu35Cd3cYn+9zVFWtIh7fS1vb9+nvf4H6+m+SSEA8fhTPm4VS
I9j2ev7qr/7kZb1EXuvzPCNn5Lh4HjQ3v5yV2LtX2IrCQrKLFzP+vvfhO/98Ci69FE6gxAcOH2Ys
aTBt2kKCwUIeeujTtLRo4PNANY7TDtxDNrsGpS7B729AawsoIRIp5KKL3s+OHd9gcLAdmEEmk0Yp
GziG1vfieWkkHLkf2I3nDaHUFExzHkpdDoziOEeRJnijSK5CCmEt9yE9JoJIyDPPSq5FNu6LkAZ5
o4jO/xTR50KEOWjOXacqd/58hLE8iNiFMSR80YiwG9LR1zBmMjSk+drXJisqbrnl72htjRMMJgmF
5uE4aYaG9mOag/h8AzjOw6RST2EYQ4RCCVw3gOcN4Th7gGa0TmBZAxQWzsZxRnHdPgDC4VJqaxvZ
vft+AoEGDGM2fX27f4NheCMOx9uhxfdvk1PFXKwARvLAIifPMDnJ5sHXeJ2i3HtGf7/L++PI6tUX
0tf3K/buvZN4PPgyJNvV1UUiAYsW/RkFBWvo7LyPeByq3C6uy3TyJ8YIszvvxsVgfXAFn+G9POob
xozWUpcaJUQPdXURlFJ0dR1jbGwUrU2EpjQQYBFFNvX8TIBipK79CJJMWQDcgCj6NgQQHEXCGuHc
teJIfLQCMS4zkEzxnQjg2IwwJBUIadWH5EfUInHY/YhnsSB33d2Y5o2EQhEqKzW9vZsoKBhj+vSL
CQYLueCCLwL/Rnv7syg1hmGkgB9gWZfi803Fth1SqbspKUnT2zuOYXyaqqoLicUqCQYr6es7yPj4
fQwPD5FIhPH752KaFj6fxcDAdh577KmTgoszckZeVUZGYMuWSUZiyxYYHQWloKlJWInPfpb0okX8
aMNm1r1wGKcnSOmaA6xKOy/rc3AiozkxEaKjowOlPolSZ6NUL4axKLcRPg8cxvOmYFmDFBQMUFpa
gNYZGhqqGRo6SjY7gWnWY1nF2LZCKru+i2zuBwEHz6vB8xYiOvwQor8bEcZxAcIuhpCmV/lQ5lZE
/z+EhEXuR4DCQQR8FCEMxn7EpixCwh9HENChEV0fyX0NIQR2b+7vehrYh1IQDNYTCFxCe/v3aGtr
o76+HgCfD4LBFI7zEJkMpNMjJJMvodROqqttiooGSKWS1NTUMXv2x+js3ExLy1bGx2cCUQxDYxgd
aK0wzUFMcxTbvph0Okp5eSPFxY8Qi7UzMND5qgzDG3U43q6OyqkCF3nu+7horV0lgyyqXssFlFIB
4GvAnVrrxO9/iX84eWUJqmV5LFwYexkVnzcyyWQ/F8y4kJljbZx14D5m9O4gi6K55EL+ue6vWVv0
ZzixmfT2tjA68E2CEyYtLU/zyU9eRWnpJTz00CGKi2vo7BzF80aRJKpShK14FvFMkoiXMAtJqPQQ
0PB/EDqxIff6xYihuSr3fQ9iiGLIRyefrxFDQizHEAPzAcSLGcnd4zASY52DGKuZSEb5IEplCQZ7
qKq6iEBgGOjCyn0qbTvFvn33MTbmYtuFBIMWZWVljI6O43nbUOooSnWRzTYTCsHERAEVFfMoLy8D
wOfzUVKylK6unzM4uJNo9INABMcZpqDAIxyuYd++vlftuHdGzgiuC/v2vZyVOHhQXispESDx+c/L
93POgcJCQHT+1lu/wDPPTGBZ5xOJVDI8nKa39xCv7HPQ0BBj3bp7UGoKmYyBbU9FqTThcCmuG0Wp
+TjOk1hWN6bZTEFBlGDwAMXFYeLxTVjWMKOjdVjWx4nFVgH7cN08a3EwlxDtR5I1M0g1l41Ua+Tn
gFyH6PRMRGenIE33LkWYTBthMA4wWSYeQfKlpiJO769QbwAAIABJREFUyzCSP/E+pNT7fOBctL4N
iZL7EZCxFMmj6kDrPmAeodB5xGINGEYxY2OPMDjYwde/fgcVFTNx3TjJpMPZZ1/I4cMbGBj4PNls
lECgnFhsNmef/RcMDDxOaek+LrzwSxQXT2fBgpt4+OF/o7l5J9lsL6YZxDT9pNNQUhJn9eqF+HyP
09HxONEo3Hrr1SxevIDe3l7q6+vPVIT9HuR1gYvcFNO/+S2naCbrDN+w5JI7785d71Nv9np/bDlZ
F88tWx6nqmrtcSNTmkzyscQRYk9ew5zhDhzTz/6py/nWgnfxbNRPbNpn2LvXozBahwKy2Q5sO4Hr
NjI+rrn33rXccsvVXHxxjB//+FdoncI0y/C8YI7BeAnxFLJMhkYshMIsRRgGjXgoLbnXzsu9Z3bu
/CQCLq5F2If1SGe+2tz1D+felwLKMc04nteD1vMQBmR67l7TkPDJOH6/TXHxFvz+TkzTpaQkgs83
lVRqmEOHnqC5uQulLqW0dBnZbC/ZbAu1tQlcN0IqJUml5eVVfPrTN/PlL/8Mn28A0zzr+P8+HE4T
Do/hOC+QyczF768nGh0iENjM9OkLcJzut0VZ2Bl5g/K978FnPwuGAQsWwMUXw9/9HaxYATNnCltx
Ern99jt4+uluwuHPUlIi+VO9vVLavGHDXlav7mLNmrVs2HCY0VGHiYlWkskteN4wrruDWOwyIpEK
Uqk04+MZTHMEn28DpaXNhEI+iotD1NfPZsmSWp57rpRw+BwcZxaOYxKLnYNtp0il/hvwYVkzMIwY
mcwQEoK4BmEp+hDQn0/2zE8kNhFwEUD0tTh3znMIGBlGbMHNQD0+XwVKVeG6XWjdi9bb0TqK1rUo
NYBhmHiejQwcvJVgsA7HGcXzhnDdMmAnjjOf4eEUjrMTCdF4bNgwk8bGOTQ11TAwcDvRaJprrvkq
TzzxdTzvHYRC8wkEhpg+/VwikQI2b/4KY2OdFBdPx7Y1Pt9q6uoWMTFxP9HoCrQuAIaoqdnKV77y
D4RCIYaHhwmFQqxZs5bvfOfe3AiHDW+rTpqnSl4vc/FNZGrNb5MWZEeqOPGgUspEAvi/kW/xivPy
wKIWeMdrZS0+97nPUZjzGvJy8803c/PNN7+Wt58y+W1dPA88cTsT7UeJPPYYbNnCUr+frnlN3L5g
MRtKZ2OWBFm1qpHr7Cz33/88jjOFiYkpjIx00df3AIZRh9+/EOimp2cGX/vaMwQCLfT2AlSglIlS
jWg9C/E4diC05xBiJAwkoSqLeCUrEdZiN5NTDT0kEcvHZAvgEJK81YZMMBxHciym5q7zJEoFMYwW
PC+M5GKEMIw9GMYqtG7H8wbQ+kWi0anMn/+n1NWVEYtV8uKLz9Ha+nMGBw/S2roPpS5Fax8zZ0qJ
2K5dAdLp7Zx33k2Mj3czNvYiN954Me9///t57rkNPProzwCOjzuOx+/ksssW09o6wPDw/YRCUwiH
LWprGykvb0Sp7rdFWdjJ5K677uKuu+562bF4/K01A+GU6/3118PChbBkiWTkvQYZGhpi3bp9+Hx1
lJQsxrKCRKNBAEZGRhkaynDnnb9i82aHysrrmTGjjtLSdjo6HmD27Mc4ePARtK5A6yUotR+f70Gm
Tq1j6dJaPv/5D1BcXAwI2zk8PMyzz7ZTWTmDsbEsmcwg2SxEImXYtoPnOYRCV5NO34uY34sQ5qAQ
CW1EkSK9fJO6MSRJuxUhn/cj9iI/AfVsxC4cQ5wUE9vuRalBlCpF6xL8fpNs9imUCqJ1Eq0nsKxZ
aD2GaU5QUjKV8fFBkslMbk1rcZxfoHUsd92jKPUXuO55HDp0AMsap77+ao4e/Rmjo4rBQaky0foo
06alGB9vo7CwgqKiUrq7HyYYLMJ1Y4yNHUWpHs455wpmzXo3qVQKw8gyMDBCKpVi6tSplJaWcscd
v/gN5+/Xv76H3t7v89GP3nJaOR5/SJ1/XeBCS4/Vod91nlJqE1CklFp0Qt7FaoQ73/Jb3pcHFjOA
i7XWI691bbfddhuLFy9+raf/weSVJahFo23M238Pc/b+kmk92/H8frjySvjZz1DXXENtYSHXDg1x
/gkJQKlUikzmDu644wE6Ou4nlZKyzFDoAmAHxcXzSaWm0N+/BdOsx+e7lIKCSxkd3Y7Wa5DY67VI
DDSBgAIfYmAiCPBwECYiPxwoPzq9AmEtfIiBieeOS+moxFuTCIDYg2EoTDNENHoOyeQBJHfDRrwd
FziA1sUYRiE+n0MgUMSBAy0oZTJtmkMsdohLL53C2NhTjI4eo7h4JfX102hqEkLMtsdpbn6Inp4f
U11dyhVXzD4eG5Vx6f/A+vX/Tk+Pn2Aww6xZNpHI2fj9QVy3j8LCEhYv/ghaO2+rsrCTyck24R07
drBkyVtnKPEp1/upU+Xrdcjw8DCOEyIctkin24lG805FIX19fbjuCHv3aior3/8bDkdp6QTB4Ivs
3v0V4vFS/H6X2tpCGhrmc9VVs142uTcvpaUBhoez2PYwRUUFmGaEROIwtj1MNusAHq6rER3O97DI
IE7FTCZzpc5CWMdhhIksR/R3H1JN1o/kZU1HbMhGhIVMoLUvN2F5GNftJxQ6B9OcjesOk8ncS2np
PNLpVtLpu4nHh7DtMiCEUkcAN9efwwGiKLUYw7gUv78Gx9G0tb3Eddcto6Pjxxw79jiuG8Cy9mCa
/bS39zE8vJlYzKO8fIwrr1zCgQP3MTSUwTT3UFOziqam6/H5QoTDYfr6dr+sz8QrnT/bTtHTs4eW
lhEOHtzHvn0DrF49/7RhMf6QOn9Kci601geVUk8CP1BKfRIJtn0HuOvEShGl1EHgb7TWD+aAxb0I
NL4a8CmlKnOnDmutbd6CUlJSQp03wjnP/yPLOl9gyrFtOGaAvbUreeri67n+9n+nJJe0lJcTE4Dy
A8vWrWumrKyBTKaZjo69ucTGZ1AqyshICePjHdi2h2Esx+erwzRD+Hzn5zrdPQSMY5pVWFaMVKoc
zzsPqXH3IzXrOxHctw4BHQUIC3E1YoR2IDkb+dkB7UjXvcsRwLGXQGArltXFjBn/QyqV4f+3d+7x
VVV3ov+u88p55XUO4eQBBBJCeEiiIApSUUBRAaW11qp0dHR0rrettZ2pY3tv1enMvdcZ26njo1M7
1lqtiq0Wiw/whRUQQSoRAhhCSAg5Cckhz5Pzfu77xz4JISbkdU6Iur6fz/4k2WevvX/ZZ//W/q3f
+q3fT1GasFqn0t19lGj0RQwGhWj0BFrtMnS6YgyGKFZrHfH4DqqrX8Vun8XXvz6flStvpqqqilDo
FbKycpg+/dTS3WnT0rHbZ/Hd715LcXHxaYaBzWbjySd/SU1NDfX19VRU7Oejj2JYLFexdOmpIkIV
FfdTVnbOl2pZmGT8UAcFZjo702huVleHGY2FdHRUEI3uoLy8iJqaOJmZny0b4Hab+PWvH+Gllzay
bdt+0tJymD49r9dN3x+73U55eS61tRXY7fPxervo7nYRje5g9erpOJ0OnM4TxGIG/P4IinKUU6u9
oqjTlXFUD0UDqlfSi9oHTEd1NM9HjcmIoer8xsT+vyb2GVG9HnXAYqLRvVgsbQixl2DwJLHYCTwe
P4WFC4FW6uqeIBYrQghIT7cjxD/gdm9FNWLuRO2LmoAChLARiWhobDyIXi9YvvyHtLYe4cCBbYTD
Jeh06/H7FTSaWszmODabnQcfXE9HRwdvv72VrVvddHTUDJpnov/g79ChjVRXN2I03owQLiKRDDZt
2sWXpR5IMkllnoubUEOV30V9el8G7u53TAnqUwzq07k28fu+xE+BGgiwHPWt9/mhrg5eegn7Sy/x
4N69hDQ6Pi28hO1X/4aPcubS0LmddeumfMaw6MtAQWHp6RdiMv0Zj+dTAoFFRKNzAB/R6ElARyxm
Q6sNEwrVEI/nIkQBEEaj2YpWW0w02omiXIbqdehGzV63BrWjMKE+EoaEBDmowV9eoAYhwmRmPk53
973E48eBa4FGhPBTVDSfoqJF7N79MyKRMF5vHJNpBQaDg0gkD7//fdLSMohEApjNVxGN7iMabaC5
OUJ6ukJOjo+bb76MpiYX//Ivv8Hrha6ukzidz6LX67DbZ/bpHOYPOILroaREXdr70ks7T5uOuuSS
6ygsnEog8CL33LNeBm1JUkLPsnOX6xgAHR0bcLn8RCLHufzyAu644zb+5V9+M2D2RqMxyvbtO2lp
UZg0aSY6XYDiYisLFpTh9/tPGz33BIrv3evE5ztCV1clVmsm5eU2li9fzI03Xs+9997H8eP7SUsz
Eg5nEInsQDUsZqN6G/+c+HkrkIZGA/H4J6geyStQV5TMRvVUHkI1JJaidsuTUZe0t6LOei8AVqLR
TMJg2I3RaEevL8DrzSMe1+F0VlFQYCUnZxaKciHFxUUcOtSE221DzSb6r0AaipJPPL6ZeNxIPB5F
iHp8vjaysowUFi4jN/c8amoqiMWKESJCLOaitHQ206eXs3Pna6xdeyUlJSVMmTIFq/XMeSb6rtaJ
xwtwOmuwWK4FHJhMPqZOPR+PJ+tLUw8kmaTMuFAUpYvBE2b1HKPt8/tx1Eiizy9Hj8JLL6nbJ5+A
yQSrVxO++25e9ofZtteJ1+vEqnUOa9TcNygsPf1cfL6TuFwngDJCoRpisWo0mjDxeHeinkA9Gk05
MI3sbCOBwAHi8aMYDMexWCaj1V5EW1s9imJBHbXEEeIoirIZ1VPxFSAdnS4PIbYSifwV1ebzADrM
5lK83v+kJ9BLo2lAo+li5sxLufba6/B626ioMNHa+jLR6EVYrecTDquGSXo6RKMOhBBEIq+i1dqw
WG4FcvD5PkCrfZ1nn92A1zurd+7TYqmmouJhamp+gc9XMqIkNINlRM3NnU1DQ+YgrSSS5HAqgVIN
7e0xdLo4y5ZdyW233YLJZBo0543d3snWrek4HNcyffpkPvnkaX71qw945ZWDlJVNZ+nSkt5VDT2e
OYfjm1x6aSEu136aml5j+fJivvOdO3nmmedpbMwkP99Id3cIRYnS2dmA6nW0o3oke7rpXNLSBBbL
xXR2TkdRtqB6KXvqCfVULG1FdS5XJn6WJIJNneh0XycUykRROvD79wCCQEDP5Ml3oNdPo7W1Aqfz
OazWGubOvYbZsxewd28LQpSi13uJREAtAb8aRekiHH4EIVzk5yvcdNN17N1rwuXaTzQawmwuIDd3
NT5fN1ptnPPOOxeNJnJa3Y7h5Jnom3+oq2sugUCYtDQTwWANpaU2zGYzGs2Xpx5IMpG1RcZKTc0p
g2LfPjCbYc0a+NGPYPVqsFoxoC7OvLJ9+MlUeoLCtNqpRCIGGhr2E4tBLOYhGMzAYpmN13uceBzg
YjSaC4nHNxGNfoLHE8VmW4nF0kQksotzzllGdnYRNTW76Ow8iEaTh05XTjBYmihc1IWag8KKVtuF
TqdBr78SRTlANBpGiBvIyPgK0ejLxGIdKMoSoAit1o5O91c6Ow9TWXkQr7cW8BEI7CYUOkI4fBCj
cQFpabsoLT2PxkYTfr+BQKCWtLSvYjDMJhxuJx5PIydnOXv2bGTJklt6PQ0FBReg0/0Yn+85vvvd
1Z+ZBjkTMre/5Gwy1IttoOyNK1fmsndvFg7HVTgcZezb9zzNzRrM5rsJBn14PBk88MCvCIV+gU43
FY+nhby86cyceQdGYyaFhcswGrPYv38jBw4c4OmnX8HlykOns6PX6ykru4y6ugo6O4Pk5FyLTmfm
+PG3EeJahNCi1x8kGq1PZPP0ocZoOVFjqtpQvRUR1FVhJ1GDL7XEYvNRlGOJ+j/ZaLVOYrGTBIN6
srJuZ+rUS4nH45jNWbS3tzF58puYzZU4nSaE8GAwVBAOV6DR5BOPH0JNvqVHr3ezfPlMHn30FxQU
FLBv3w95551foNHk09VVj9v9OOnpK5g50zFgPEUPQ+WZ6Pkutm7dQShUhaJsp7R0UW+cl+wzRoc0
LkZDdfUpg6KyUjUo1q6F//2/1eBMi2XAZiNJptITFBYOH8fjqcFsvgqjMZNAoI5Q6ABmswaLZTpw
GybTfITQ4vFYiES2EIm8gMfzF4qK0igpycZo1ODzHScnp4tIJEBn5ydEo5kYjUaCwSri8QZgJjpd
mEmTitBq44RC7QSDOnS6OcTjFvz+3cTj9SjK1QhhRqezIoQBrXYp4fBb7N79Cj5fBYoSIx4vIB73
EwhsJhZ7C7t9Gc3NWjyeN5k+fRYtLT4iER/B4G4UxY/NFmb27EV88MHr6PWnR+Srozoz2dnZIxo1
9B2RBINd6PVWIhEvbveuL3UQp2R8GUznBzI+1JUfT2K3R2lvr+l10RuNs3C7d1NZ2cbJk4sxGKxM
mfId3O5qnM43effd+7jmml/i9/uJxdJpbw/x+9+/wJEjOrKyLkWvn0E43MSJE3/FbNbR1hYnLW0x
GRk2mpu3EwzWYzYvRK+3EY02o77cP0VdLt6CWpL9OtRqpu+hGhfp6HTTiUZVI0RRAsTjeSjKPozG
t9FoNIRCEArt5ujREyjKCsJhP6rX08qiRXq2bPklwaALmIxOF0any8Zsfhyvt55I5E0sFjd+v4Gd
Oz8iEgnjchUwY8ZyOjuN+HxVuN17yMjwUlx834BZNYfLqe/iSp566nds29ZEXt4iYjE/HR1frnog
yUQaF8OluxseeUQ1KA4cUA2Iq6+G++9XDQqzOSmXaW8/VY7ZYoFYrAshjqDOZxqJxRqBj4hGFQyG
KUQidoQwEY+7MRoNZGVdTiRyiOJiM5MmzcRqNVNenktnZxde71zmzv0nnM6/Uln5Nm73a2Rk+AmF
POh0BqZPX0dGRg7BoJujRzcAAYqK1hMK5dLWthe/X6B6LAJkZ5cTCp0gEKglEjlCJFKNolgwGJag
0djRaFqJxcLEYk6s1ig6XTVWq5dQyEl6eiE6XRaKkkModIJ586ag1/sxmcJEIqevPHa59uP3N1Ff
Xz/i9LlXX30VH3xwHzt2fEAgYMBkCnPxxdO4+uo7kvJdSSRjpcf4CAQCvPjiSxw6VEUs9gwGQxy3
28PUqfkEg27i8QDNzX5MpkvRajsxGAxYLBcSDKZz/Pgv+eCD1+jsVJdfxuN7qKjw4PMV4nb/CUXx
oNWmYTDkoNO1YbX6iMV24ffPIjPThFqG/SSRiJKo21FDPJ5BWtr/Ixj8V1TvxWbUjL1q2QC9fg1G
I8RidoLBbUAtJtNGhDiMTpdPUdE6qqvjeL3ZRCIfYzC8gdG4CKNRR0dHgLq6eiZNWsy0aRaam21E
ox6EaMLr3U40WkJ29nqmTp3EyZPP8txznxCJNDNnzr04HGrsiceziAMHptDW9jz19Q9ht5vHHKBt
t9u5665v43B8eeuBJBNpXAwXgwGeeAIuuQR++lO48ko1piJJ9M/iabVCMHgCMJGRYScQ2IDbfZxI
pBmNpg23W49e70WnO0w06gVcpKV14fE0EA5raW6+BKv1fBTFyObNb+DzVTJnzv04HGUUFFxAWdkN
fPrpy3g8m/F4MujqasNg6AQyiEYbiUYPo9Mp+P2tRKMF6PVTUeNrj6PT5WAwZGMyFaDV+vD7Q8Tj
UfT6K9DrbwamEo0eRYgXUZQTzJlTTmnpNXR21lNT8wsikXoaGn6D1Xoxs2bNJicnQnv7+1x8cSHt
7btwubIwmyezd++THDz4NhqNiQMHHmXq1DTWr1/Dt751w7CWhb322hba26exePHNGAyTCYdP0t7+
Pq+9tkVGfksmFH/840a2bnWTl3cLTU1WIpEgHs9vaWh4nYyMmdhsehob9RiNAdSpCT1WqyAYzMPn
i1FVdYDMzCUI0QwYaWnJRKNZTihkRaOJE48fJh7XE49nM39+FJvNSVeXk1hMQyTiw+d7ioyMGEKk
YzLNxu93EIuB0fgrwuF/Jh6vQY3RcpOTY8dorKat7UNMplk4HEtRlMsoK8ukttZKKDSP8vLLaW5+
l6YmH4pSQjy+hbS0KGZzmNzc+ezZs4/Fi/+ec84p4/XXN3P0qCAedxCPbyQzs5jS0hUIESQatZOW
lkdd3THKy3MAMJvNicqlq6mpqeTOO1ewYMGCpHgWvuz1QJKJNC6Gi9EIDQ2gHV3MafsQ8RYDZfH0
eDaSkfEuQmQRDjeh0ZiwWr9ONJpPNNpIPP4HIpFn0ekuIjMzM+GKPEJOzmVkZNxAXV0Ner2ejIxL
qa7eQ3l5OqCm1T5y5E3q66tpbe1Gp0tj0iQ9sdhLuN1a4vEgGRlWfL4ZdHS8jtmci8GQgxAGFOU1
otFFBAIz0Gg8RKNvIsRJhLCh1a5Fqy0jFosB89FofMTj76MoaoEgjUaHz1fCnXeuYPfuv3LwYA3R
qBMh1NHB1VffkSh3vpGdOw9y9Ggc+CZ5eZeh0XhoaHiFJ554G4PBMKRxMFDyMpiBy2WSkd+SCUXf
Z3XOnDkcOlSF09mB251Ld/crzJhxA7Nmnc/Bg3+lu3sbBoONhoZ6hAgTi9USj59ApzuMyRTG4cjF
6ZyDXp+L31+dyI5pJBbrIhqtw26/kBkzvKSlnaC6OoZOdzF5eSuwWj1oNBWEQgfp7l6I2Ryiu3sH
Wu0q4H8RCLyAwfAX8vPziUZzaG5uIRz2Eo06gSwKChYzefIUPv00hsXioKmpGZ0uH6PRSzweJh73
Eom8Q3p6KSUl62lo+BSDYTImk4k1a67ijTe24/Fk0dmZyYwZ89Dr0/B6qzEYID9/EVVVr3PyZA3Z
2Xm9983tPo7dnpY0w6IvX9Z6IMlEGhcjoL2ra8TW7EAeif6pZc+UxTMQqEFRKgmHg2RlfYvW1gBC
OMjMzCEU0hAIPIlG8xadnSEcjiIyMyPk599BWpqaIsTprGLhwkJiMYWqqo0UFl5MQ8NHHDhwGL9/
LvH4DIT4gFAoh/PPn8fUqXaCQQ0ffrgDn+84dvssIpE3iURC6HR1RCJBFKUTt/t9NJoIJlOE6dOt
1NYKYjFBLOZFnVf1EYuBVptGZqaahKgnMGrevHksW7ZsQIPrllvWc9FFNdxzz8N0dJxLRsY6rFb1
f9Fq0/D7n2Tr1v2sXXvlGb+DwVaLZGbKyG/JxKGmpoadO3fS3Oxh3rxC9Ho9555bxqxZftraHFRW
/oiCgj0Eg9WYzW/g82mBvyES8RGJOInH38JkamXlyjuZNKmUQKADp7MFvf4k8XgUne5GDIYSotEq
otHHyc7uIho1ARlccskN6HQ2hAiQnV2AxzOPqqp/Jxj8EL//QqxWA17vU4RCJzAa2/na18qorj7M
nj1xTKZ/xGIx4fNV09m5F5PpTaLR64hEjmO1enC5rGRmziEYjBIO16PRzMLhWEEstoOTJw9gMPgJ
h08CMzCbzZSU5FNR8TFabTfhsB+vtxKfbwulpSVotTqmTk2ju/t9XK6sQXNWDIehBnmS5CGNi2Ew
HANhMAbySKhL0E4lZel5EebkpNPe3lPi2IzBkIPDMYNp06I0NjYSDrcRi8UxGk2EwzoMhivQak9g
sUynpeUlcnNziUYziUROkpaWi9GYSWdniH37fk1HxzE++OBP7Nq1lXC4GSHOJS1tIQ5HPtGoFpfr
ILt3d9HYeA6hUDudnVuIRl1kZf0jJpMDn+8godBbKMpMDIbLyMtzEI02EQh8wMKFJqLReurrPyIS
MSFEBmo2z91YLAKbbeaAAVdnGh3EYqbEyOfUslG1BH06nZ2eIY0DuVpEkgxS9TLq6Ojg3nvvY8eO
BrxeBa+3jaNHf8811/xdok8JEAgcZe7cUu677w46OzuJxTrYvr2G9vZXgUJ0urSE4QA1NVuYNu0i
ADQaP5FIG1rtFQgxDUXRotE4MJkuJhbbRywWJBbLxOutpKWliXBYnfXNzS3Abp/C5Zdn884722hs
DJCR4SUnR3Djjddz2WWXct11P8JmuxFFmUs0GsViUQiHA3R1/RG/X3D55QXU1R3A5fKTkTEDrbaS
UOgv2O2FBAJOWlv34XJVk5Xl4cCBUzlscnIi5OTsxWxupKvrZ6Sn51JUVEZOTgku1xbWr1+DwWAY
dSzEWPpwyehImXEhhMhGTaK1FjWJ1p+AuxVF8Q2z/RPA3wPfVxTl0VTJORyGYyAMxJk8En1d8yaT
iRMnDlJR8XO8Xh3BYACjcTIWSwGZmftZufJq5s/vQKPJoro6issVIC1tIeBCCANW6xKMxg46O48x
c2Ypx46p6+djMROdnX+ioeEwOt2l2GxX4/EYCIf/ikZTRXZ2Bbm5i4Bb6e5+ALd7E253LXZ7Ljk5
5VRXv09b24NkZ59Dd3cl8bgJjcZCNLoNn8+Gw5HFjBnz0eu93H77XP7rvz6moyNKPD4Zvd6FwbCb
0lIbra3PjKgzsNlsZGfrURQXwaC7ty5DMHgc8JCdbRrSOOi7WgQY02hH8uUj1S+je++9jzfeCJCV
9Q9MmTKXhoZHOXZsO3/+c5iZM9Opq6vE43Exc6aeDz/cw4IFZUSjRiZPPg+7fSUaTQ5G42QMhixq
an7FsWNvcfz4dhyOckymGJHICdLTc1AUL0L4UZQmMjKKCAbfp6xsPtu3V9LQYMBmu4HMzEKCweNU
Vb3ItGm13Hnnr7nzTqitrQXoXQL+zjvvEAwamTbtIrRaG5FIBL2+kGCwmJaWrXzjGxezZs0annji
Nzz00G9xuV5Bq1VIS4vi9dYSDDrQ61cwf/5ipkzRU1n5+Gk5bL73vYu46KLvs3Hjqxw65CIabUKI
pt5+w2QyjToWYrR9uGT0pNJz8QJq9pWVqCkffwf8miESawEIIb4GXIiaA/asMlwDYSCG65rfunUb
Ho+DtrY5RCLl6HQKbvfLtLW9CGTw4x//CYMhQFraP2O3rycUsqAo1cAHZGRMJhZzU1hYREfHXqzW
SRQVaTl27Ek6O+vw+RqIxUrQ6dYSi80hIyOO369Ho7EQjzckyrKbgBJMphoWL76J3NzZgBmNZi7H
j/8ek6kLj2caWu0UDIa/x2oNYDAcJy+vgLKQqnvZAAAcUUlEQVSychoaHuaqq1bhcOSyefPHtLYe
JyfHzOrVN7By5SUEAoERdQZ2u52VK+dz6NCHtLdricWWAl243a+Qnd3GypVrh3WugXIJyMhvyXBI
5cuopqaGHTsayMr6ByZPXg5AcfFPgP+D0/krursvICtrBeXls8nPN7Jp07t4vR50ugB+vwaH43x0
OtWj5/W6cDiKMRjs+P0v0dDwHkVFcbq6okQi1fh87YTDISwWAyaTm9xcA9/4xtfYvr06UdDQgTqN
6Uj8fRwY2KuYmZmJVuuls7OSvLzL0ev1AHR21pGeDuXl5ZhMquE/efJs2ttLyM5eAYQ5duyXGAwK
S5ZcxgUXnA+A0Zg+YA6be+/9x0E9RqOJhRhLHy4ZPSkxLoQQs1Fzxy7sKVwmhLgLeEMI8cO+9UUG
aFsAPJJovzkV8o2EsczdD8c13/Pgz527nvb2Rnw+D0KYCYcPEY2WYbH8LVptAVZrO62tT6PVPoXJ
ZCMctmO1ziQrayGFhRlkZxs4dsyA0bgHnc7M+eebaG3V8vHH+Wi1MzAaS4jFuggEFHS6NKJRC8Fg
G8HgcUIhL6HQX8jOnoHPl82HH9YSDoMQZrTaCO3t1eh0V2MwHMJq7WLq1GUEAsW4XFW0tBzGaoX8
/Hzmz5/P2rVXJsWNfP311xKJhHnuuXdobHwVCDNtmpH169cM2ziQkd+S0ZDql1F9fT2BgIFJk0rw
+/3o9Xr0ehN5ed/C7X6X2bPXsWjRWsyJ5e06nZ79+zeyYEEhH330AR0dFb1l3H2+GnJzw5SUlHDP
ParRYzKZ+OlPH+Stt3aSlraErKzJZGYGsNmauOGG1RiNRiZPnoHFUkJLSxVutzotMnduCVbr0c/0
aX29OEK4aWz8bzweLwUFi/H5DtPV9XvWrCmkpKSk995dcMG3aW3V43R24PH40WjOIz29jtLSU0Xg
zpTDJpkBlTL+6uyQKs/FEqCzT0VUUGuMKKgeiU0DNRJCCOBZ4CFFUarUP88uY5m7H45rvqamx+2a
R3p6GIejnECghu5uAzrdN7FYlhOLtZOdPQe9Xk8k8hA331zO/v0wadIqJk8uIRxuxeX6C7feurr3
5Q7wr//6JJmZJ2lpOUgo9GiiJHKEeFyPEBGgFo/nWSCA0ViD2Xw+x44FsVjmkJmZSUfHLiIRhZwc
OxdccA2NjekcO7aHQMCOTuegvb2WEyeOsX79nGHFUYwEk8nE7bffyte+ds1n3LMjRUZ+S0ZCql9G
ubm5hMOt1NbuxGC4EK0WMjNNRCIfodWaKClZhNlsxu/3EwgEMBhyaG2F1auv4OjRY7z77jO4XHVY
LA5yc4Okpx9h6dKS3lo5zzzzPCdP5jFz5hQ6Ohrp7j5EU1MdpaUFXH/9vfj9frKydNjt6cybN5NA
IIDJZMLjOUospvtMn9bXi7NmzS28886PcTofIhTKICdHz5o1hYmKxH3v3UwKCjKZNctPc3Mdu3cf
JxaLE416UEu1j1/8k4y/OjukyrjIRc0P24uiKDEhRAc9T9bA/AgIK4ryeIrkGjFjnbsfyjXf8+CH
wycxGCAWCxONthOLadHpilCUGFot6PV6TKYS3G4dCxaUMX++ws6d79Ha+t5p5zSZTL1GSzRqxmLR
EY1aicfL0Ou/gqK4iEafIyPjIHPn5mCzxcjOzgTK2LZtPxbLeYnMnUdQlD0UFS2htXUf4fBJzjvv
RgyGjTidG2lv70SrrWXdurWjnmYYTrCcNAwk402qX0YVFZWkpcXo7n4DrdYGzKSpaRtCvEp+vg5F
6WDfPg9OZwfhMESjtdhsn9LVtZIHHvgx5577Otu3HyQaPYrdnnZaxdQez0F+/rXYbCV88skzRCKH
gGns2dPMb3/7DLfddkufPu2qRJ92dMA+bSAvzje/+SLV1a/hdv+Rf/7nu04rItj33mm1JRw58gpO
Zw1dXfX4/VXs2fMUX/nK9/H7T45b/JOMvzo7jMi4EEI8CNx7hkMUYM5oBBFCLAS+B5w3mvY/+MEP
yMw8vSDVQLXrR8NY5u6Hcs2fevDfJz19OlVVJ/H7TxCLuVCUarzeTPLyrLS3d9DSspN4/CSbNu1i
9erF3H//7YPGM9hsNnQ6P6GQAYfjetxuQSj0CfE4pKVNYfbsLp544gGMRiM2m40TJ05w5MhPCQbf
xu3ehsEApaUlFBevZOfO73LixGuYTCZmz15LdrZaIGndurV85zt3jvh+ysjticGGDRvYsGHDafvc
bvdZkmZ0pELvU/ky6nlZL1/+IPv3/4GGhkcIhw1otR5ycz3cdts3+MMffktHxyKyspYiRAdtbfto
bT3JPfc8QlnZOSxdWsJ//Mc/Dqj7fb0uhw5t5NgxNxbLHaSnO2hvf51Nm45htW4cdp82mBensHAZ
DQ17yc7OHvTeVVe/gdMZwecrJxSaiVY7nU8//YS2tm9yySUXs27dnHGLf5LxVyrjqfMj9Vz8HHh6
iGPqUBPST+67U6g1eW2JzwbiK6g1vp19pkO0wC+EEN9XFKXoTBd9+OGHWbBgwRCijY5kzN2faQTe
8+A/9dSfE0vIwGjsJBx+hUgkRltbEZHICRTlDWbOnI/Ndkei49t2WnBZf0/AvHkO3nuvnpycBeTm
TqK720kg4KSk5FJycsBoNJ5Wdrys7BwikRVYrXmYTDbMZjsuVyVz55aycOEU9u8/pZjr1587asXs
HyzX0nKY559/Da/3mVEZK5LRMdBLuKKigoULF54liUZOqvR+rC+jwbxyp17W5VxzzTLa29VRvclk
x+t9lcWLF7F58y4Cgb1Eo/V4PO3o9TYyMn5EMLiNSGQFmzbtor/u99DjOXC59vfWJrFay/B6XWRk
FJOffw47d25h7Vr/sPq00Xhxrr/+WrzeZ3jssTfo7l5BKBTCbi8kN/erdHR8gM/3n5SWZo3rKg0Z
f6Uynjo/IuNCUZR2oH2o44QQu4AsIcR5feIuVqLmj/5okGbPAu/02/d2Yv9QBs24kCoXvbrE6kq2
bt1PQcFNTJo0G6+3hXfffQCX61G6utLQ68Pk5dlYseJpMjMLgFPBZWazeUBPwNe/vo4tWypwubYT
jRZjNkNp6VRyciIIcXrHcGrEsQuj8So0Gl1vboqVK6eyatVKVq1Sjx2LYvZ1s9psPdkIA3R3z+Cx
x14B6C1LLZGcLUb7MhrKK9f/ZW23l2C3l/RW9DQajeTnn0N5+S34/R727DmGXr8Yo9GI270bqzUP
o/GqQQNLe/T4+edfo7s7jN3uwOt14fOpJcRzcwtpaNjSGzcyVJ82XC9Of2Nq1aqVvPlmDTU1UzAa
LyArS/V85OQsIRJ5lW3b9nPttTWnDW7GAznNOn6kJOZCUZTDQoi3gCeFEP8TdSnqY8CGvitFhBCH
gXsVRdmkKEonauYl+nweAVoURalJhZwTCbUKqjlRNjkTp3MPVusVGAy5NDcfIC9vIQZDA8eOvc+5
567vDS6rra3l/fd3sG2bj2nT+i+bg1tvXc0f/1hLRkZJn+DPdwd07/YfrRmNEez2LvbuzWbnzudP
6yjH8n+ecttWUV3djcUyB7t9Du3tlWzaVIvVKteeSyYGI30ZDbWEdaiXdXFxcSIGy4PRWEA83oHR
mEkweASDAUwmGxqN7oyBparnwMNjj71Be/vrZGQUU1pqY968OTQ1VRCLjcwNfiYvzmDG1MqVl2A2
x4nFunsz7MZiERob36G7u57KSg0/+cl/sXr1+XI69AtKKvNc3ISaROtd1CRaLwN39zumBMhkcJTU
iDa+DCdwse+IJh4v6HVppqVl4nbrSU+/GJ2uA6dzI7NmtdPZWc+JEzX8x3/8no8/rsdg+Cp6Pdhs
5t7Aq507N3L//bcnfv9s8Gd/+o/W3n57K1u3ZuBwXMXkyclZ69/zf7a0HMbpDGCxzMFqdeD1VpKR
kU1BwQp27nxPrj2XfO4Y7hLWM72sTSZTr/GRkXEpWq2Xjo5dKMoeSktLeqcqzxRYajKZeqcXN206
Rn7+Odjt+Xz44Sbq61/H4fDys589P+w4pzN5cZ555vlBjKltLFtWyp49O+joKMJmW0Bj4zu0t28m
Pf08Jk1agsmUw6ZN75OqRFYy1ffZJWXGhaIoXQyRMEtRlDNWARsqzmKiM5LAxb4jmq6uuQQCYdLS
TIRCTqZNyyQQqEcIB6FQGKfzQ44ceROIk5e3irS0XaSlLaO62gVUce65Zb2ejUAgMGL3bs/n+/e3
JH2t/+lu2xnY7XNOqyPgcJTT0PCeXHsu+dwx3CWsQ025nDI+tmA0HqOry01R0YUUF68cMI3+YNx2
2y1Yrep5du48RkuLep7zzrsVv//kiAcK/b04QxlT999/O/v2HeCddx4hGMynu7ue9PTzSE9fwfTp
OUyfXpaSQoIyYHxiIGuLpJCRZvnr6VS2bt1BKFSFomyntHQRpaULqa6uobp6O5FIJfG4j/R0FyUl
/0R2djFHjuxFiAAWSwlOZxWzZvnxeE4PuBqpezeVa/1PBXy9Qnu76rEoLS1h3rxr6eiokWvPJZ9L
Rhr8OJhO9jU+Tpw4wfbtO9m/v4Xm5idGtVLtootq+MlPHmXOnL+jsHAZAOnpakaAsbzYa2traW72
UFSUc9r+vgObRx/9Ob/97TO88cZOKis1TJq0hOnTc5g3bw5+v59YLJ329lBSBxMy1ffEQBoXKWI0
Wf5OdSpX8tRTv2Pbtiby8hYhRJi8PIhEmrjkkuVceunF/Od/bsZuL8VozGTq1BKqq7dgNK4gFPLi
dH5MKLRrTMvmUrnW/3S3bS0FBStwOMrp6KiRa88ln1uSvYS1x/iYP3/+mF38Wq0dh6P8tH2jHSj0
eAa2bt3Pp58e4ejRzZSWLmLePDXRX98+okfXV61ayU9+8l+YTDkUFJwqK9/dXYtWe4C3397KlClT
xuxZkKm+Jw7SuEgRYxn52+127rrr2zgcp8/LXn+9OmLx+/2nvfjnzVM9HkeOPEs43IReP4srr5w/
psDL8Ug8c8pt+x4NDWeOB5FIPg+kKp/CWFY5JHugcMoz8C1mz/6Iqqpa9u/XEol4mDYtfcA+oqSk
hNWrz2fTpvc5ftxJU5MVnS4NIZrJz1/K1q3upARyy1TfEwdpXKSIsSr0meZl+wZ9gao4eXnziUSq
WbZsOrff/rdJUaBUJ56Ra88lXzTG8kynKgAxmQOF/p4Bm60EvX4jR47sprr6Vez2WaxbN/DA5tR0
6O9QlGJMpmymTj01HZoMz4JM9T1xkMZFikiWQg82YhnoxX/99aVJDVoar5e/XHsu+aIxkmd6PAIQ
kzVQ6O8Z0OtNnHvuegoLL6Ku7hd897vXnpYOvC8mk4lVq1by3nt12O03kJVViNms3qNkeRZkqu+J
gzQuUkgqR/7jOeqXL3+JJHWMRwBisvqLwTwD4bCHvDw7xcXFQ7a3281otbpewwKS61mQqb4nBikz
LoQQ2ah5Ltai5rn4E3C3oii+IdrNAf4NuCQh3yHg64qiNKZK1lQxHgaAfPFLJJ9fUh2A2H+qZaz9
xVg9A+PhWZDTrRODVHouXgAcqGm/DcDvgF9zhtwXQohiYAfwJHAf4AHmAcEUyplypAEgkUgGIlUB
iKmcahmrZ2C8PAuy3z27pMS4EELMBq4AFvbUFhFC3AW8IYT4Yd8U4P34P8AbiqL8uM++Y6mQUSKR
SM42qQpATOVUy1g9A9Kz8OVAk6LzLgE6+xQtAzUNuAJcOFADoZZCXQPUCCHeFEK4hBC7hRDrUiSj
RCKRnFV6pglcri24XJUEg+7eLJxLl45umuDUVMtVOBxlGI2ZOBxlOBxXsXNnDe3tQ9aeHLbsJSWj
n8oYa3vJxCZVxkUucLLvDkVRYkBH4rOBmAxYgXuBzcDlwCvARiHExSmSUyKRSM4q119/LevWTSEW
20hDw8PEYhtZt27KqKcJeqZaMjM/O9Xi9aqfSySpZkTTIkKIB1Ff/oOhAHNGKUuPofNnRVEeTfxe
KYS4CLgTNRZDIpFIvlAke5pA5nqQTARGGnPxc+DpIY6pA1pQPRG9CCG0gC3x2UC0AVGgqt/+KmDp
UIL94Ac/IDPz9AKrN954IzfeeONQTSWSLyUbNmxgw4YNp+1zu0dWjvts80XS+2QFIMpcD5LBGE+d
F4qS/KrmiYDOQ8D5fQI6V6FOd0wZLKBTCLETOKooyi199m0E/IqiDLjKRAixANi7d+9eFixYkOT/
RCL5clFRUcHChQtBDcauONvyDIbU+zMjK4NKhkuqdD4lq0UURTkshHgLeFII8T9Rl6I+Bmzoa1gI
IQ4D9yqKsimx62fAi0KIHcBfgKtQ82Rckgo5JRKJ5IvIRF2RkaoU55KJRyrzXNyEmkTrXdQkWi8D
d/c7pgTo9WkqivJnIcSdwP8CHgGqgWsVRdmVQjklEonkC8lEyfUgPSlfPlJmXCiK0sUZEmYljtEO
sO93qAm3JBKJRPIFYDxSnEsmFqlaiiqRSCQSybjl3ZBMLKRxIZFIJJKUIfNufDmRxoVEIpFIUkbf
vBt9kXk3vthI40IikUgkKSMVKc4lE59UrhaRSCQSiWTcKqFKJg7SuJBIJBJJSpmoeTckqUNOi6SA
/ulVzyZSloGRskiSyUT6DieSLHC6PGe7EupEujcTSZZUkDLjQgiRLYR4XgjhFkJ0CiF+I4SwDNHG
IoR4XAjhFEL4hRCHhBD/I1UypoqJ9NBIWQZGyiJJJhPpO5xIssDEkkfKMn6k0nPxAmqF1JXAGmAZ
8Osh2jwMrELN7jk78ffjQoi1KZRTIpFIJBJJEkmJcZEoXHYF8HeKonysKMqHwF3ADUKI3DM0XQI8
oyjKDkVRGhRF+Q2wH7ggFXJKJBKJRCJJPqnyXCwBOnsqoiZ4F1CAC8/Q7kPgGiFEPoAQYjlq/ZG3
UiSnRCKRSCSSJJOq1SK5wMm+OxRFiQkhOhKfDcZdwH8DjUKIKBAD7lAUZecZ2hgBqqqqxiZxEnG7
3VRUTIxq1VKWgZGyDEwfPTKeTTmGwYTS+4n0HU4kWWBiySNl+Swp03lFUYa9AQ+iVjgdbIsBs4Af
A1UDtHcB/+MM5/8hUAWsBs4Bvg10AyvO0OYmVI+I3OQmt+RtN42kbxjvDan3cpNbsrek6rxIKOqw
EELYgaHWENUBfwP8XFGU3mOFEFogCFynKMqmAc5tBNzAVxVF2dJn/5NAgaIoq88g0xVAfeL8Eolk
9BiB6cBbiqJM2IpSUu8lkqSREp0f0bRI4sJDXlwIsQvIEkKc1yfuYiUggI8GaaZPbLF++2OcITYk
IdMLQ8kkkUiGzYdnW4ChkHovkSSVpOt8SgI6FUU5jBqE+aQQYpEQYinwGLBBUZSWnuOEEIeFEOsS
bTzANuDnQohLhBDThRB/C9wMbEyFnBKJRCKRSJJPKtN/3wQ8jrpKJA68DNzd75gSILPP399Ejet4
DrABx4EfK4ry3ymUUyKRSCQSSRIZUcyFRCKRSCQSyVDI2iISiUQikUiSijQuJBKJRCKRJJXPpXEx
mqJoiXZzhBCbhBBdQgivEOIjIcSUsyFLn/ZPCCHiQojvjUWO0cgihNAJIf5dCFGZuB9NQohnhBB5
o7z+d4QQx4QQASHEbiHEoiGOv1QIsVcIERRCHBFC3DKa645VFiHE14QQbwshTibu3YdCiFVnQ5Z+
7ZYKISJCiKRl2hnFd2QQQvxfIUR94nuqSwRajztS75MjSzL1fiLp/EjlkXp/xuPHrvdnOxnOKBPo
bAEqgPOBi4AjwHNDtCkG2lADRsuAGcBaYNJ4y9Kn7deATwAn8L3xvi9ABuqqnq+jBtdeAOwG9ozi
2t9EzTdwM2rRuV8DHYPdX9R11V7gIaAU+A4QAS5Pwn0YqSwPoyZwW5h4Tv4vEALKx1uWPu0ygaM9
3+lY5RitLMAm1GVqy4FpqOn7lyRDnlQ/34k2Uu8/e3xS9H4i6fwo5ZF6P3ibMev9mAUf7y1xc+LA
eX32XQFEgdwztNuAWhTtrMuSOK4AaECtHHtsrJ3MWGTpd57zUXOLTBnh9XcDj/T5WwCNwD8Ncvy/
A5UDfEebk/C9jEiWQc5xEPjJ2ZIlcS9+CjyQxE5mpN/RlYlOKCsZ1x+j7FLvkyxLv/OMWO8nks6P
Rp5BziH1Pkl6/3mcFhlxUTQhhEAt+14jhHhTCOFKuIbWjbcsfeR5FnhIUZRkFUcYbbG4/mQl2nQN
t4EQQo9q/W/t2aeoT+m7CbkGYnHi8768dYbjUylL/3MIIB1VwcZdFiHEragj7J+O5fpJkOVq4GPg
XiFEoxCiWgjxM6Fm0x1vpN4nUZYBGJHeTySdH4M8/c8h9V4lKXr/eTQuBiyKhvpADFYUbTJgBe4F
NgOXA68AG4UQF4+zLAA/AsKKojw+hmsnS5ZehBBpwL8BLyiK4h3BtScBWtTaMX1xneHauYMcn5GQ
Y7SMRpb+3ANYgD+OQY5RySKEKAH+H7BeUZT4GK8/JlmAIuBiYB7wVdQ8NdcBv0yiXMNF6n1yZell
lHo/kXR+tPL0R+q9SlL0fsIYF0KIBxMBToNtMSHErFGevuf//LOiKI8qilKpKMq/A68Dd46nLEKI
hcD3gFuHeXwq70vf6+iAl1BHL98e6/k+rwghbgLuA76hKErbOF9bAzwPPKAoSm3P7vGUoR8aVJf7
TYqifKwoypvAPwC3JOFlAEi9P8PxUu/HEan3p5EUvU9lhs6R8nPg6SGOqQNaUEckvQi1KJot8dlA
tKHOQfZ3RVYBS8dZlq8AOYBT9cIBqmX5CyHE9xVFKRpHWXqO6+lgpqJWoB2J1wLU+xsDHP32O85w
7ZZBju9WFCU0wuuPVRYAhBA3AP+NWlzvL2OQYbSypKPOfZ8rhOgZJWhU0UQYWKUoyvvjJAtAM9DU
73moQu34pgC1A7YaGVLvP596P5F0frTyAFLvByA5ep+MgJHx3FADmGKcHsC0iqEDu3bSL7ALtWbJ
sCK8kyULkA3M7bc1orrESs7CfdGhuor3A7YxXH+goCEncM8gx/8bsL/fvhdIXUDnoLIkjrkR8AFr
k/y8DluWxGf9n41fAp+iBgCaxvO+AHegRveb++xbhxrhn5bM+zQM2aXeJ/e+jFnvJ5LOj0aexDFS
7z97fFL0Pmk3czw31PnTj4FFqCOQauD3/Y45DKzr8/dXUZfj3I667Oi7QJgxLqsbjSwDnGPMUeOj
kSXRwWxCreEyH9Wa7dn0I7z29YCf05c7tQM5ic8fpE8nj7oszYMaQV6K6pINA5cl4T6MVJabEte+
s989yBhvWQZon8yo8ZHeF0vi2fgDaie3LPFMPZEMeVL9fCf+lnqvpEbvJ5LOj1IeqfcD35ek6P2Y
BT8bG2pk83OAG+gEnqSPlZU4Jgbc3G/f36KuAfehrgsfs7U6Wln6fV6XpE5mRLIAhYm/+27xxM9l
o7j+t4F6IADsAs7v89nTwHv9jl8G7E0cXwP8TRKfkWHLAvxlgPsQA3473rIM0DZpncwov6NZqBH9
3kSH8xDj7LUY7fPdZ5/U+xTp/UTS+ZHKI/X+jN/TmPVeFi6TSCQSiUSSVCbMahGJRCKRSCRfDKRx
IZFIJBKJJKlI40IikUgkEklSkcaFRCKRSCSSpCKNC4lEIpFIJElFGhcSiUQikUiSijQuJBKJRCKR
JBVpXEgkEolEIkkq0riQSCQSiUSSVKRxIZFIJBKJJKlI40IikUgkEklS+f8/dDvDvjbFdgAAAABJ
RU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
```

