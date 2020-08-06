(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-09690447"],{

/***/ "38c6":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishDetailNode.vue?vue&type=template&id=7ca95c30&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',[_c('div',[_c('span',[_vm._v(_vm._s(_vm.$socket.connected ? 'Socket connected' : 'Socket disconnected'))]),_c('span',[(_vm.$socket.disconnected)?_c('span',{staticClass:"notification",staticStyle:{"color":"red"}},[_c('el-divider',{attrs:{"direction":"vertical"}}),_vm._v("You are disconnected\n      ")],1):_vm._e()]),_c('el-divider',{attrs:{"direction":"vertical"}}),_c('el-switch',{attrs:{"active-text":"自动滚动","inactive-text":"取消"},on:{"change":_vm.scroll_publish},model:{value:(_vm.scroll_switch),callback:function ($$v) {_vm.scroll_switch=$$v},expression:"scroll_switch"}})],1),_c('el-divider',{staticStyle:{"margin":"10px 0"},attrs:{"content-position":"left"}},[_vm._v("发布日志如下：")]),_c('div',{staticClass:"publish_detail"},[_c('el-scrollbar',{ref:"el_scrollbar",staticStyle:{"height":"100%"}},[_c('div',{ref:"log_output",staticClass:"publish",style:(_vm.publish_style),domProps:{"innerHTML":_vm._s(_vm.log_output)},on:{"scroll":function($event){return _vm.scroll_publish(false)}}})]),_c('el-backtop',{attrs:{"target":".publish","bottom":100}},[_c('div',{staticStyle:{"{\n      height":"100%","width":"100%","background-color":"#f2f5f6","box-shadow":"0 0 6px rgba(0,0,0, .12)","text-align":"center","line-height":"25px","color":"#1989fa"},attrs:{"id":"publish_div"}},[_vm._v("UP")])])],1)],1)}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/PublishDetailNode.vue?vue&type=template&id=7ca95c30&scoped=true&

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

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishDetailNode.vue?vue&type=script&lang=js&



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


/* harmony default export */ var PublishDetailNodevue_type_script_lang_js_ = ({
  data: function data() {
    return {
      log_output: "",
      scroll_switch: true,
      scroll_top: 0,
      publish_style: {
        overflowY: "auto",
        width: "1300px",
        height: "550px"
      }
    };
  },
  sockets: {
    connect: function connect() {
      console.log("socket connected");
    }
  },
  methods: {
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
        var _this = this;

        var reconnect;
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
                // 当首次cookie为空时，写完cookie后重连websocket（其他改进策略：换原生websocket，更好的掌控整个websocket生命周期）
                // 终极改进：TODO 用户登录后，直接用会话的cookie标识
                reconnect = this.getCookie("publish_client_id") == "";
                _context.next = 6;
                return http["a" /* default */].post("/publishNodejs", {
                  id: this.$route.query.id
                }).then(function (response) {
                  _this.$message({
                    showClose: true,
                    message: "正在发布...",
                    type: "success"
                  });

                  if (reconnect) {
                    _this.$socket.client.disconnect();

                    _this.$socket.client.connect();
                  }
                }).catch(function (error) {
                  _this.$message.error("请求失败");
                }).then(function () {});

              case 6:
                this.$socket.client.emit("publish_event", {
                  id: this.$route.query.id,
                  type: "nodejs"
                });
                this.$socket.$subscribe("publish_response_nodejs_" + this.getCookie("publish_client_id") + "_" + this.$route.query.id, function (data) {
                  if (data.message) {
                    _this.$message({
                      message: data.message,
                      type: "warning"
                    });
                  }

                  if (data.data && _this.$refs.log_output) {
                    _this.$refs.log_output.innerText += data.data;

                    _this.scroll_publish(null);
                  }

                  if (data.status && data.status == "OK") {
                    var h = _this.$createElement;

                    _this.$notify({
                      title: "发布状态",
                      message: h("i", {
                        style: "color: green"
                      }, data.project + "发布结束，详情请查看发布日志")
                    });
                  }
                });

              case 8:
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
      var _this2 = this;

      if (!this.scroll_switch) {
        return;
      }

      var div = this.$refs.log_output; // socket调用时，加载时机的问题处理

      if (!div) {
        return;
      } // console.log("=====" + this.scroll_switch + ", " + manual_switch + ", " + div.scrollTop + ", " + div.scrollHeight);
      // 如果人为打开开关，则自动滚动


      if (manual_switch != null && manual_switch || div.scrollTop >= this.scroll_top) {
        this.$nextTick(function () {
          div.scrollTop = div.scrollHeight;
          _this2.scroll_top = div.scrollTop; // 标记当前滚动的位置，为下次识别是否人为滚动做准备
        });
      } else {
        // 如果人为向上滚动，则停止自动滚动
        this.scroll_switch = false;
      }
    },
    resize_div: function resize_div() {
      // console.log('================' + document.documentElement.clientHeight + ', ' + document.documentElement.clientWidth);
      var height_used = this.$refs.log_output.getBoundingClientRect().top;
      this.publish_style.height = "".concat(document.documentElement.clientHeight - height_used - 1, "px");
      this.publish_style.width = "".concat(document.documentElement.clientWidth * 0.95, "px");
    }
  },
  mounted: function mounted() {
    // document.getElementById("nodejs").className =
    //   document.getElementById("nodejs").className + " el-menu-item is-active";
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
// CONCATENATED MODULE: ./src/views/PublishDetailNode.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_PublishDetailNodevue_type_script_lang_js_ = (PublishDetailNodevue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/PublishDetailNode.vue?vue&type=style&index=0&id=7ca95c30&scoped=true&lang=css&
var PublishDetailNodevue_type_style_index_0_id_7ca95c30_scoped_true_lang_css_ = __webpack_require__("c830");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/PublishDetailNode.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_PublishDetailNodevue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "7ca95c30",
  null
  
)

/* harmony default export */ var PublishDetailNode = __webpack_exports__["default"] = (component.exports);

/***/ }),

/***/ "c830":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetailNode_vue_vue_type_style_index_0_id_7ca95c30_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("f790");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetailNode_vue_vue_type_style_index_0_id_7ca95c30_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetailNode_vue_vue_type_style_index_0_id_7ca95c30_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishDetailNode_vue_vue_type_style_index_0_id_7ca95c30_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

/***/ }),

/***/ "f790":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ })

}]);
//# sourceMappingURL=chunk-09690447.af783d9c.js.map