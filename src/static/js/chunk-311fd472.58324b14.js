(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-311fd472"],{

/***/ "48a1":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "4ad2":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_UpdatePublishStatic_vue_vue_type_style_index_0_id_f2a74e82_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("48a1");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_UpdatePublishStatic_vue_vue_type_style_index_0_id_f2a74e82_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_UpdatePublishStatic_vue_vue_type_style_index_0_id_f2a74e82_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_UpdatePublishStatic_vue_vue_type_style_index_0_id_f2a74e82_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

/***/ }),

/***/ "6e67":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/UpdatePublishStatic.vue?vue&type=template&id=f2a74e82&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"publish"},[_c('el-form',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],ref:"form",attrs:{"model":_vm.publishment,"rules":_vm.rules,"label-width":"200px"}},[_c('el-form-item',{attrs:{"label":"发布名称"}},[_c('el-input',{attrs:{"placeholder":"eg: develop_youxuan_supplier_web"},model:{value:(_vm.publishment.name),callback:function ($$v) {_vm.$set(_vm.publishment, "name", $$v)},expression:"publishment.name"}})],1),_c('el-form-item',{attrs:{"label":"描述"}},[_c('el-input',{attrs:{"placeholder":"eg: 妈妈优选供应商web端（线下环境）"},model:{value:(_vm.publishment.description),callback:function ($$v) {_vm.$set(_vm.publishment, "description", $$v)},expression:"publishment.description"}})],1),_c('el-form-item',{attrs:{"label":"git仓库地址"}},[_c('el-select',{attrs:{"filterable":"","placeholder":"请选择"},on:{"click":function($event){return _vm.list_git_repos()},"change":function($event){return _vm.resetBranch()}},model:{value:(_vm.publishment.git_repo_id),callback:function ($$v) {_vm.$set(_vm.publishment, "git_repo_id", $$v)},expression:"publishment.git_repo_id"}},_vm._l((_vm.git_repo_options),function(item){return _c('el-option',{key:item.value,attrs:{"label":item.label,"value":item.value}})}),1),_vm._v("*\n    ")],1),_c('el-form-item',{attrs:{"label":"git分支"}},[_c('el-select',{attrs:{"multiple":"","placeholder":"请选择（单选）"},on:{"focus":function($event){return _vm.get_git_repo_branches()}},model:{value:(_vm.publishment.git_branches),callback:function ($$v) {_vm.$set(_vm.publishment, "git_branches", $$v)},expression:"publishment.git_branches"}},_vm._l((_vm.git_branch_options),function(item){return _c('el-option',{key:item.value,attrs:{"label":item.label,"value":item.value}})}),1)],1),_c('el-form-item',{attrs:{"label":"发布文件位置（相对）","prop":"source_file_dir"}},[_c('el-input',{attrs:{"placeholder":"eg: assets"},model:{value:(_vm.publishment.source_file_dir),callback:function ($$v) {_vm.$set(_vm.publishment, "source_file_dir", $$v)},expression:"publishment.source_file_dir"}})],1),_c('el-form-item',{attrs:{"label":"目标服务器"}},[_c('el-select',{attrs:{"multiple":"","filterable":"","allow-create":"","placeholder":"请选择或输入（单选）"},on:{"focus":function($event){return _vm.change_ip_group()}},model:{value:(_vm.publishment.to_ip),callback:function ($$v) {_vm.$set(_vm.publishment, "to_ip", $$v)},expression:"publishment.to_ip"}},_vm._l((_vm.to_ip_options),function(group){return _c('el-option-group',{key:group.label,attrs:{"label":group.label}},_vm._l((group.options),function(item){return _c('el-option',{key:item.value,attrs:{"label":item.label,"value":item.value}})}),1)}),1)],1),_c('el-form-item',{attrs:{"label":"目标服务器项目目录"}},[_c('el-input',{attrs:{"placeholder":"eg: /data/project/mama_[project_name]"},model:{value:(_vm.publishment.to_project_home),callback:function ($$v) {_vm.$set(_vm.publishment, "to_project_home", $$v)},expression:"publishment.to_project_home"}})],1),_c('el-form-item',[_c('el-button',{attrs:{"type":"primary"},on:{"click":_vm.onSubmit}},[_vm._v("修改")])],1)],1)],1)}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/UpdatePublishStatic.vue?vue&type=template&id=f2a74e82&scoped=true&

// EXTERNAL MODULE: ./node_modules/core-js/modules/web.dom.iterable.js
var web_dom_iterable = __webpack_require__("ac6a");

// EXTERNAL MODULE: ./src/util/http.js
var http = __webpack_require__("adb5");

// EXTERNAL MODULE: ./node_modules/q/q.js
var q = __webpack_require__("4be7");

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/UpdatePublishStatic.vue?vue&type=script&lang=js&

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


/* harmony default export */ var UpdatePublishStaticvue_type_script_lang_js_ = ({
  data: function data() {
    return {
      publishment: {
        name: null,
        description: null,
        git_repo_id: null,
        git_branches: null,
        profile: null,
        source_file_dir: null,
        to_ip: null,
        to_project_home: null
      },
      git_repo_options: [],
      git_branch_options: [],
      profile_options: [{
        value: "dev",
        label: "开发环境（dev）"
      }, {
        value: "test",
        label: "测试环境（test）"
      }, {
        value: "pre",
        label: "预发环境（pre）"
      }, {
        value: "online",
        label: "生产环境（online）"
      }],
      to_ip_options: [{
        label: "线下",
        options: [{
          value: "192.168.1.248",
          label: "192.168.1.248"
        }, {
          value: "192.168.1.249",
          label: "192.168.1.249"
        }, {
          value: "192.168.1.251",
          label: "192.168.1.251"
        }]
      }, {
        label: "预发",
        options: [{
          value: "47.96.18.198",
          label: "47.96.18.198"
        }]
      }, {
        label: "线上",
        options: [{
          value: "114.55.232.195",
          label: "114.55.232.195"
        }, {
          value: "118.178.128.57",
          label: "118.178.128.57"
        }, {
          value: "47.110.153.206",
          label: "47.110.153.206"
        }, {
          value: "47.110.154.253",
          label: "47.110.154.253"
        }]
      }],
      rules: {
        name: [{
          required: true,
          message: "请输入发布名称",
          trigger: "blur"
        }, {
          min: 3,
          max: 50,
          message: "长度在3到50个字符",
          trigger: "blur"
        }],
        description: [{
          required: true,
          message: "请输入发布名称",
          trigger: "blur"
        }, {
          min: 5,
          max: 100,
          message: "长度在5到100个字符",
          trigger: "blur"
        }],
        git_repo_id: [{
          required: true,
          message: "请选择git仓库地址",
          trigger: "change"
        }],
        git_branches: [{
          required: true,
          message: "请选择git分支名称",
          trigger: "change"
        }],
        profile: [{
          required: true,
          message: "请选择发布环境",
          trigger: "change"
        }],
        to_ip: [{
          required: true,
          message: "请选择目标服务器ip",
          trigger: "change"
        }],
        to_project_home: [{
          required: true,
          message: "请输入目标服务器项目主目录",
          trigger: "blur"
        }]
      },
      loading: false
    };
  },
  methods: {
    get_publishment: function get_publishment() {
      var _this = this;

      http["a" /* default */].get("/publishmentStatic/" + this.$route.query.id).then(function (response) {
        _this.publishment = response.data;
      });
    },
    list_git_repos: function list_git_repos() {
      var _this2 = this;

      this.loading = true;
      http["a" /* default */].get("/git/repos").then(function (response) {
        _this2.git_repo_options.length = 0;
        response.data.forEach(function (repo) {
          _this2.git_repo_options.push({
            value: repo.id,
            label: repo.ssh_url_to_repo + " (" + repo.description + ")"
          });
        });
      }).catch(function (error) {
        _this2.$message.error("查询失败");
      }).then(function () {
        _this2.loading = false;
      });
    },
    get_git_repo_branches: function get_git_repo_branches() {
      var _this3 = this;

      if (!this.publishment.git_repo_id) {
        return;
      }

      this.loading = true;
      http["a" /* default */].get("/git/repo/" + this.publishment.git_repo_id + "/branches").then(function (response) {
        _this3.git_branch_options.length = 0;
        response.data.forEach(function (branch) {
          _this3.git_branch_options.push({
            value: branch,
            label: branch
          });
        });
      }).then(function () {
        _this3.loading = false;
      });
    },
    change_ip_group: function change_ip_group() {
      if (!this.publishment.profile) {
        return;
      } // if (this.publishment.profile == 'dev') {
      //   this.to_ip_options.length = 0;
      //   this.to_ip_options.push(this._to_ip_options[0]);
      // } else if (this.publishment.profile == 'pre') {
      //   this.to_ip_options.length = 0;
      //   this.to_ip_options.push(this._to_ip_options[1]);
      // } else if (this.publishment.profile == 'online') {
      //   this.to_ip_options.length = 0;
      //   this.to_ip_options.push(this._to_ip_options[2]);
      // }

    },
    sleep: function sleep(ms) {
      return new Promise(function (resolve) {
        return setTimeout(resolve, ms);
      });
    },
    resetBranch: function resetBranch() {
      this.publishment.git_branches = null;
    },
    onSubmit: function onSubmit() {
      var _this4 = this;

      http["a" /* default */].request({
        url: "/publishmentStatic",
        method: "POST",
        data: this.publishment
      }).then(function (response) {
        _this4.$message({
          showClose: true,
          message: "修改成功",
          type: "success"
        }); // this.sleep(1200).then(() => {
        //   this.$router.go(0);
        // });


        _this4.get_publishment();
      }).catch(function (error) {
        _this4.$message.error("保存失败");
      });
    }
  },
  mounted: function mounted() {// document.getElementById("static").className =
    //   document.getElementById("static").className + " el-menu-item is-active";
  },
  created: function created() {
    this.list_git_repos();
    this.get_git_repo_branches();
    this.get_publishment();
  }
});
// CONCATENATED MODULE: ./src/views/UpdatePublishStatic.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_UpdatePublishStaticvue_type_script_lang_js_ = (UpdatePublishStaticvue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/UpdatePublishStatic.vue?vue&type=style&index=0&id=f2a74e82&scoped=true&lang=css&
var UpdatePublishStaticvue_type_style_index_0_id_f2a74e82_scoped_true_lang_css_ = __webpack_require__("4ad2");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/UpdatePublishStatic.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_UpdatePublishStaticvue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "f2a74e82",
  null
  
)

/* harmony default export */ var UpdatePublishStatic = __webpack_exports__["default"] = (component.exports);

/***/ })

}]);
//# sourceMappingURL=chunk-311fd472.58324b14.js.map