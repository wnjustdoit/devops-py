(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-5d46a730"],{

/***/ "7f7f":
/***/ (function(module, exports, __webpack_require__) {

var dP = __webpack_require__("86cc").f;
var FProto = Function.prototype;
var nameRE = /^\s*function ([^ (]*)/;
var NAME = 'name';

// 19.2.4.2 name
NAME in FProto || __webpack_require__("9e1e") && dP(FProto, NAME, {
  configurable: true,
  get: function () {
    try {
      return ('' + this).match(nameRE)[1];
    } catch (e) {
      return '';
    }
  }
});


/***/ }),

/***/ "c2a8":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "c6ef":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishDetail.vue?vue&type=template&id=2f682086&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',[_c('div',{staticStyle:{"margin-top":"10px"}},[_c('el-breadcrumb',{attrs:{"separator-class":"el-icon-arrow-right"}},[_c('el-breadcrumb-item',[_vm._v("后端发布")]),_c('el-breadcrumb-item',{attrs:{"to":{ path: '/publishList' }}},[_vm._v("发布列表")]),_c('el-breadcrumb-item',[_vm._v("发布详情")]),_c('el-breadcrumb-item',[_vm._v(_vm._s(this.$route.query.name))])],1)],1),_c('div',{staticStyle:{"margin-top":"5px","text-align":"right","font-size":"12px","margin-right":"15px"}},[(_vm.socket.connected)?_c('span',{staticStyle:{"color":"blue"}},[_vm._v("Socket connected")]):_vm._e(),(_vm.socket.disconnected)?_c('span',{staticStyle:{"color":"red"}},[_vm._v("Socket disconnected")]):_vm._e(),_c('el-divider',{attrs:{"direction":"vertical"}}),_vm._v("自动滚动日志：\n    "),(_vm.socket.connected)?_c('el-switch',{on:{"change":_vm.scroll_publish},model:{value:(_vm.scroll_switch),callback:function ($$v) {_vm.scroll_switch=$$v},expression:"scroll_switch"}}):_vm._e()],1),_c('el-divider',{attrs:{"content-position":"left"}},[_c('span',{staticStyle:{"font-size":"12px"}},[_vm._v("发布进度")])]),_c('el-steps',{staticStyle:{"font-size":"12px"},attrs:{"active":_vm.active,"finish-status":"success","align-center":""}},[_c('el-step',{attrs:{"title":"准备环境"}}),_c('el-step',{attrs:{"title":"从git克隆工程"}}),_c('el-step',{attrs:{"title":"maven打包"}}),_c('el-step',{attrs:{"title":"检查上传环境"}}),_c('el-step',{attrs:{"title":"上传远程服务器"}}),_c('el-step',{attrs:{"title":"执行远程发布脚本"}}),_c('el-step',{attrs:{"title":"发布收尾工作"}})],1),_c('el-divider',{attrs:{"content-position":"left"}},[_c('span',{staticStyle:{"font-size":"12px"}},[_vm._v("发布日志")])]),_c('div',{staticClass:"publish_detail",attrs:{"id":"terminal"}},[_c('el-scrollbar',{ref:"el_scrollbar",staticStyle:{"height":"100%"}},[_c('div',{ref:"log_output",staticClass:"publish",style:(_vm.publish_style),domProps:{"innerHTML":_vm._s(_vm.log_output)},on:{"scroll":function($event){return _vm.scroll_publish(false)}}})]),_c('el-backtop',{attrs:{"target":".publish","bottom":100}},[_c('div',{staticStyle:{"{\n      height":"100%","width":"100%","background-color":"#f2f5f6","box-shadow":"0 0 6px rgba(0,0,0, .12)","text-align":"center","line-height":"25px","color":"#1989fa"},attrs:{"id":"publish_div"}},[_vm._v("UP")])])],1)],1)}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/PublishDetail.vue?vue&type=template&id=2f682086&scoped=true&

// EXTERNAL MODULE: ./node_modules/core-js/modules/es6.function.name.js
var es6_function_name = __webpack_require__("7f7f");

// EXTERNAL MODULE: ./node_modules/regenerator-runtime/runtime.js
var runtime = __webpack_require__("96cf");

// EXTERNAL MODULE: ./node_modules/@babel/runtime-corejs2/helpers/esm/asyncToGenerator.js
var asyncToGenerator = __webpack_require__("3b8d");

// EXTERNAL MODULE: ./node_modules/core-js/modules/es6.regexp.split.js
var es6_regexp_split = __webpack_require__("28a5");

// EXTERNAL MODULE: ./src/util/http.js
var http = __webpack_require__("adb5");

// EXTERNAL MODULE: ./node_modules/querystring-es3/index.js
var querystring_es3 = __webpack_require__("b383");

// EXTERNAL MODULE: ./node_modules/socket.io-client/lib/index.js
var lib = __webpack_require__("8055");
var lib_default = /*#__PURE__*/__webpack_require__.n(lib);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishDetail.vue?vue&type=script&lang=js&




//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//



/* harmony default export */ var PublishDetailvue_type_script_lang_js_ = ({
  data: function data() {
    return {
      log_output: "",
      scroll_switch: true,
      scroll_top: 0,
      publish_style: {
        overflowY: "auto",
        width: "99%",
        height: "550px"
      },
      active: -1,
      steps: {
        $step0: 0,
        $step1: 1,
        $step2: 2,
        $step3: 3,
        $step4: 4,
        $step5: 5,
        $step6: 6,
        $step7: 7
      },
      socket: {
        connected: false,
        disconnected: true
      }
    };
  },
  methods: {
    getStepIndex: function getStepIndex(lineContent) {
      if (lineContent != null && lineContent.indexOf("$step") != -1) {
        for (var key in this.steps) {
          if (lineContent.indexOf(key) != -1) {
            return this.steps[key];
          }
        }
      }

      return null;
    },
    getCookie: function getCookie(cookieName) {
      var strCookie = document.cookie;
      var arrCookie = strCookie.split("; ");

      for (var i = 0; i < arrCookie.length; i++) {
        var arr = arrCookie[i].split("=");

        if (cookieName == arr[0]) {
          return arr[1];
        }
      }

      return "";
    },
    publish_init: function () {
      var _publish_init = Object(asyncToGenerator["a" /* default */])(
      /*#__PURE__*/
      regeneratorRuntime.mark(function _callee() {
        var _this2 = this;

        var socket;
        return regeneratorRuntime.wrap(function _callee$(_context) {
          while (1) {
            switch (_context.prev = _context.next) {
              case 0:
                if (this.$route.query.id) {
                  _context.next = 3;
                  break;
                }

                this.$message({
                  message: "发布ID不可为空",
                  type: "warning"
                });
                return _context.abrupt("return");

              case 3:
                _context.next = 5;
                return http["a" /* default */].post("/publish", {
                  id: this.$route.query.id
                }).then(function (response) {
                  if (response.data.status == "FAILED") {
                    _this2.$message({
                      message: "请先登录",
                      type: "warning"
                    });

                    var _this = _this2;
                    setTimeout(function () {
                      _this.$router.push({
                        path: "/userLogin"
                      });
                    }, 1000);
                    return;
                  }

                  _this2.$message({
                    showClose: true,
                    message: "开始发布...",
                    type: "success"
                  });
                }).catch(function (error) {
                  console.error(error);
                }).then(function () {});

              case 5:
                socket = lib_default()("ws://192.168.1.248:5000");
                this.socket = socket;
                socket.on("connect", function () {
                  socket.emit("publish_event", {
                    id: _this2.$route.query.id
                  });
                });
                socket.on("publish_response_" + this.getCookie("session_id") + "_" + this.$route.query.id, function (data) {
                  if (data.message) {
                    _this2.$message({
                      message: data.message,
                      type: "warning"
                    });
                  }

                  if (data.data) {
                    _this2.log_output += data.data + "<br/>";

                    var stepIndex = _this2.getStepIndex(data.data);

                    if (stepIndex != null) {
                      _this2.active = stepIndex;
                    }

                    _this2.scroll_publish(null);
                  }

                  if (data.status && data.status == "OK") {
                    var h = _this2.$createElement;

                    _this2.$notify({
                      title: "发布状态",
                      message: h("i", {
                        style: "color: green"
                      }, _this2.$route.query.name + "发布成功，详情请查看发布日志"),
                      duration: 0
                    });
                  }

                  if (data.status && data.status == "FAILED") {
                    var _h = _this2.$createElement;

                    _this2.$notify({
                      title: "发布状态",
                      message: _h("i", {
                        style: "color: grey"
                      }, _this2.$route.query.name + "发布失败，详情请查看发布日志"),
                      duration: 0
                    });
                  }
                });

              case 9:
              case "end":
                return _context.stop();
            }
          }
        }, _callee, this);
      }));

      function publish_init() {
        return _publish_init.apply(this, arguments);
      }

      return publish_init;
    }(),
    scroll_publish: function scroll_publish(manual_switch) {
      var _this3 = this;

      if (!this.scroll_switch) {
        return;
      }

      var div = this.$refs.log_output; // socket调用时，加载时机的问题处理

      if (!div) {
        return;
      } // 如果人为打开开关，则自动滚动


      if (manual_switch != null && manual_switch || div.scrollTop >= this.scroll_top) {
        this.$nextTick(function () {
          div.scrollTop = div.scrollHeight;
          _this3.scroll_top = div.scrollTop; // 标记当前滚动的位置，为下次识别是否人为滚动做准备
        });
      } else {
        // 如果人为向上滚动，则停止自动滚动
        this.scroll_switch = false;
      }
    },
    resize_div: function resize_div() {
      var height_used = this.$refs.log_output.getBoundingClientRect().top;
      this.publish_style.height = "".concat(document.documentElement.clientHeight - height_used - 1, "px");
      this.publish_style.width = "".concat(document.documentElement.clientWidth * 1 - 38, "px");
    }
  },
  mounted: function mounted() {
    // 自适应窗口
    this.resize_div();
    window.onresize = this.resize_div; // js修改样式

    document.getElementsByClassName("el-scrollbar__view")[0].style += ";overflow-x: hidden;";
    document.getElementsByClassName("el-divider--horizontal")[0].style.margin = "8px 0";
  },
  created: function created() {
    this.publish_init();
  }
});
// CONCATENATED MODULE: ./src/views/PublishDetail.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_PublishDetailvue_type_script_lang_js_ = (PublishDetailvue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/PublishDetail.vue?vue&type=style&index=0&id=2f682086&scoped=true&lang=css&
var PublishDetailvue_type_style_index_0_id_2f682086_scoped_true_lang_css_ = __webpack_require__("e9a7");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/PublishDetail.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_PublishDetailvue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "2f682086",
  null
  
)

/* harmony default export */ var PublishDetail = __webpack_exports__["default"] = (component.exports);

/***/ }),

/***/ "e9a7":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetail_vue_vue_type_style_index_0_id_2f682086_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("c2a8");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetail_vue_vue_type_style_index_0_id_2f682086_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetail_vue_vue_type_style_index_0_id_2f682086_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetail_vue_vue_type_style_index_0_id_2f682086_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

/***/ })

}]);
//# sourceMappingURL=chunk-5d46a730.c6d3971a.js.map