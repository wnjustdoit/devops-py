(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-022238c6"],{

/***/ "54df":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "5e8a":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/NewUser.vue?vue&type=template&id=1e7971e9&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"user"},[_c('el-form',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],ref:"user",attrs:{"model":_vm.user,"rules":_vm.rules,"label-position":"right","label-width":"200px"}},[_c('el-form-item',{attrs:{"label":"用户昵称","prop":"nick_name"}},[_c('el-input',{attrs:{"placeholder":"eg: 流川枫"},model:{value:(_vm.user.nick_name),callback:function ($$v) {_vm.$set(_vm.user, "nick_name", $$v)},expression:"user.nick_name"}})],1),_c('el-form-item',{attrs:{"label":"登录名","prop":"login_code"}},[_c('el-input',{attrs:{"placeholder":"eg: liuchuanfeng"},model:{value:(_vm.user.login_code),callback:function ($$v) {_vm.$set(_vm.user, "login_code", $$v)},expression:"user.login_code"}})],1),_c('el-form-item',{attrs:{"label":"密码","prop":"login_pwd"}},[_c('el-input',{attrs:{"placeholder":"eg: 123456"},model:{value:(_vm.user.login_pwd),callback:function ($$v) {_vm.$set(_vm.user, "login_pwd", $$v)},expression:"user.login_pwd"}})],1),_c('el-form-item',{attrs:{"label":"用户邮箱","prop":"email"}},[_c('el-input',{attrs:{"placeholder":"eg: wn@company.com"},model:{value:(_vm.user.email),callback:function ($$v) {_vm.$set(_vm.user, "email", $$v)},expression:"user.email"}})],1),_c('el-form-item',{attrs:{"label":"gitlab邮箱","prop":"gitlab_email"}},[_c('el-input',{attrs:{"placeholder":"eg: wn@company.com"},model:{value:(_vm.user.gitlab_email),callback:function ($$v) {_vm.$set(_vm.user, "gitlab_email", $$v)},expression:"user.gitlab_email"}})],1),_c('el-form-item',{staticStyle:{"text-align":"left"},attrs:{"label":"角色","prop":"role"}},[_c('el-select',{attrs:{"filterable":"","placeholder":"请选择"},model:{value:(_vm.user.role),callback:function ($$v) {_vm.$set(_vm.user, "role", $$v)},expression:"user.role"}},_vm._l((_vm.roles),function(item){return _c('el-option',{key:item.value,attrs:{"label":item.label,"value":item.value}})}),1)],1),_c('el-form-item',{staticStyle:{"text-align":"left"}},[_c('el-button',{attrs:{"type":"primary"},on:{"click":_vm.onSubmit}},[_vm._v("立即创建")]),_c('el-button',{on:{"click":function($event){return _vm.resetForm('ruleForm')}}},[_vm._v("重置")])],1)],1)],1)}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/NewUser.vue?vue&type=template&id=1e7971e9&scoped=true&

// EXTERNAL MODULE: ./src/util/http.js
var http = __webpack_require__("adb5");

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/NewUser.vue?vue&type=script&lang=js&
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

/* harmony default export */ var NewUservue_type_script_lang_js_ = ({
  data: function data() {
    return {
      user: {
        nick_name: null,
        login_code: null,
        login_pwd: null,
        email: null,
        gitlab_email: null,
        role: null
      },
      roles: [{
        value: "backend",
        label: "后端开发"
      }, {
        value: "frontend",
        label: "前端开发"
      }, {
        value: "devops",
        label: "运维人员"
      }],
      rules: {
        nick_name: [{
          required: true,
          message: "请输入用户昵称",
          trigger: "blur"
        }, {
          min: 2,
          max: 12,
          message: "长度在2到12个字符",
          trigger: "blur"
        }],
        login_code: [{
          required: true,
          message: "请输入登录名",
          trigger: "blur"
        }, {
          min: 5,
          max: 30,
          message: "长度在5到30个英文字符",
          trigger: "blur"
        }],
        login_pwd: [{
          required: true,
          message: "请输入登录密码",
          trigger: "blur"
        }, {
          min: 5,
          max: 30,
          message: "长度在5到30个英文字符",
          trigger: "blur"
        }],
        email: [{
          required: true,
          message: "请输入用户邮箱",
          trigger: "blur"
        }, {
          min: 5,
          max: 30,
          message: "长度在5到30个英文字符",
          trigger: "blur"
        }],
        gitlab_email: [{
          required: true,
          message: "请输入gitlab邮箱",
          trigger: "blur"
        }, {
          min: 5,
          max: 30,
          message: "长度在5到30个英文字符",
          trigger: "blur"
        }],
        role: [{
          required: true,
          message: "请选择角色",
          trigger: "change"
        }]
      },
      loading: false
    };
  },
  methods: {
    onSubmit: function onSubmit() {
      var _this = this;

      this.$refs["user"].validate(function (valid) {
        if (valid) {// console.log("submit!");
        } else {
          // console.log("error submit!!");
          return false;
        }
      });
      http["a" /* default */].request({
        url: "/admin/user",
        method: "PUT",
        data: this.user
      }).then(function (response) {
        _this.$message({
          showClose: true,
          message: "保存成功",
          type: "success"
        });

        _this.$router.push({
          path: "/userList"
        });
      }).catch(function (error) {
        _this.$message.error("保存失败");
      });
    },
    resetForm: function resetForm() {
      this.$refs["user"].resetFields();
    }
  }
});
// CONCATENATED MODULE: ./src/views/NewUser.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_NewUservue_type_script_lang_js_ = (NewUservue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/NewUser.vue?vue&type=style&index=0&id=1e7971e9&scoped=true&lang=css&
var NewUservue_type_style_index_0_id_1e7971e9_scoped_true_lang_css_ = __webpack_require__("997f");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/NewUser.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_NewUservue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "1e7971e9",
  null
  
)

/* harmony default export */ var NewUser = __webpack_exports__["default"] = (component.exports);

/***/ }),

/***/ "997f":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_NewUser_vue_vue_type_style_index_0_id_1e7971e9_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("54df");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_NewUser_vue_vue_type_style_index_0_id_1e7971e9_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_NewUser_vue_vue_type_style_index_0_id_1e7971e9_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_NewUser_vue_vue_type_style_index_0_id_1e7971e9_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

/***/ })

}]);
//# sourceMappingURL=chunk-022238c6.f79cb294.js.map