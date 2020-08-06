(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-40853b9e"],{

/***/ "254a":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ }),

/***/ "2fa2":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_GitRepoList_vue_vue_type_style_index_0_id_59c097ce_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("254a");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_GitRepoList_vue_vue_type_style_index_0_id_59c097ce_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_GitRepoList_vue_vue_type_style_index_0_id_59c097ce_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_GitRepoList_vue_vue_type_style_index_0_id_59c097ce_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

/***/ }),

/***/ "54d3":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/GitRepoList.vue?vue&type=template&id=59c097ce&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],staticClass:"gitRepoList"},[_c('div',{staticStyle:{"text-align":"right"}},[_c('el-alert',{ref:"tips",staticStyle:{"width":"100%","height":"40px"},attrs:{"type":"info","description":"双击表格行展开/收缩列。","show-icon":""}}),_c('el-button',{attrs:{"type":"text","plain":"","size":"mini"},on:{"click":function($event){return _vm.updateGitRepo2Db()}}},[_vm._v("更新 Git 仓库信息")]),_c('el-button',{staticStyle:{"margin-left":"20px","margin-right":"10px"},attrs:{"type":"text","plain":"","size":"mini"},on:{"click":function($event){return _vm.list_projects_web_hooks()}}},[_vm._v("Web Hook 管理")])],1),_c('div',{staticStyle:{"text-align":"left"}},[_c('el-table',{ref:"dataTable",staticStyle:{"width":"100%","margin-top":"7px"},attrs:{"data":_vm.gitRepoList,"border":"","max-height":"580","cell-style":_vm.cellStyle,"header-cell-style":_vm.headerCellStyle},on:{"row-dblclick":_vm.doubleClickRow}},[_c('el-table-column',{attrs:{"type":"expand"},scopedSlots:_vm._u([{key:"default",fn:function(props){return [_c('el-form',{staticClass:"table-expand",attrs:{"label-position":"left","inline":""}},[_c('el-form-item',{attrs:{"label":"id"}},[_c('span',[_vm._v(_vm._s(props.row.id))])]),_c('el-form-item',{attrs:{"label":"name"}},[_c('span',[_vm._v(_vm._s(props.row.name))])]),_c('el-form-item',{attrs:{"label":"description"}},[_c('span',[_vm._v(_vm._s(props.row.description))])]),_c('el-form-item',{attrs:{"label":"name_with_namespace"}},[_c('span',[_vm._v(_vm._s(props.row.name_with_namespace))])]),_c('el-form-item',{attrs:{"label":"path"}},[_c('span',[_vm._v(_vm._s(props.row.path))])]),_c('el-form-item',{attrs:{"label":"path_with_namespace"}},[_c('span',[_vm._v(_vm._s(props.row.path_with_namespace))])]),_c('el-form-item',{attrs:{"label":"ssh_url_to_repo"}},[_c('span',[_vm._v(_vm._s(props.row.ssh_url_to_repo))])]),_c('el-form-item',{attrs:{"label":"http_url_to_repo"}},[_c('span',[_vm._v(_vm._s(props.row.http_url_to_repo))])]),_c('el-form-item',{attrs:{"label":"web_url"}},[_c('span',[_vm._v(_vm._s(props.row.web_url))])]),_c('el-form-item',{attrs:{"label":"web_hooks"}},[_c('span',[_vm._v(_vm._s(props.row.web_hooks))])])],1)]}}])},[_c('template',{slot:"header"},[_c('el-button',{attrs:{"type":"text","icon":"el-icon-more"}})],1)],2),_c('el-table-column',{attrs:{"width":"45","prop":"id","label":"id"}}),_c('el-table-column',{attrs:{"sortable":"","prop":"path_with_namespace","label":"path_with_namespace"}}),_c('el-table-column',{attrs:{"sortable":"","prop":"description","label":"description"}}),_c('el-table-column',{attrs:{"prop":"web_url","label":"web_url"}}),_c('el-table-column',{attrs:{"width":"95","label":"操作"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [_c('el-button',{attrs:{"type":"danger","round":"","size":"mini","icon":"el-icon-delete"},on:{"click":function($event){return _vm.deleteItem(scope.row.id)}}},[_vm._v("删除")])]}}])}),(_vm.showWebHook == true)?_c('el-table-column',{attrs:{"sortable":"","prop":"web_hooks","label":"Web Hooks"}}):_vm._e(),(_vm.showWebHook == true)?_c('el-table-column',{attrs:{"width":"120","label":"Web Hook操作"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [(scope.row.web_hooks == '[]')?_c('el-button',{attrs:{"type":"text","plain":"","round":"","size":"mini"},on:{"click":function($event){return _vm.add_gitlab_web_hook(scope.row, scope.$index)}}},[_vm._v("添加Web Hook")]):_vm._e(),(scope.row.web_hooks != '[]')?_c('el-button',{staticStyle:{"color":"red"},attrs:{"type":"text","round":"","size":"mini"},on:{"click":function($event){return _vm.delete_gitlab_web_hook(scope.row, scope.$index)}}},[_vm._v("删除Web Hook")]):_vm._e()]}}],null,false,316667496)}):_vm._e()],1)],1)])}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/GitRepoList.vue?vue&type=template&id=59c097ce&scoped=true&

// EXTERNAL MODULE: ./node_modules/core-js/modules/web.dom.iterable.js
var web_dom_iterable = __webpack_require__("ac6a");

// EXTERNAL MODULE: ./src/util/http.js
var http = __webpack_require__("adb5");

// EXTERNAL MODULE: ./src/assets/common.js
var common = __webpack_require__("8e9a");

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/GitRepoList.vue?vue&type=script&lang=js&

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


/* harmony default export */ var GitRepoListvue_type_script_lang_js_ = ({
  data: function data() {
    return {
      gitRepoList: [],
      total: 0,
      currentPage: 1,
      pageSize: 10,
      keyword: null,
      loading: false,
      showWebHook: false
    };
  },
  methods: {
    cellStyle: function cellStyle() {
      return Object(common["b" /* cellStyleLeft */])();
    },
    headerCellStyle: function headerCellStyle() {
      return Object(common["c" /* headerCellStyle */])();
    },
    doubleClickRow: function doubleClickRow(row, column, event) {
      this.$refs.dataTable.toggleRowExpansion(row);
    },
    list_git_repos: function list_git_repos() {
      var _this = this;

      http["a" /* default */].get("/git/repos", {}).then(function (response) {
        _this.gitRepoList = response.data;
      }).catch(function (error) {
        _this.$message.error("查询失败");
      });
    },
    deleteItem: function deleteItem(id) {
      var _this2 = this;

      this.$confirm("确认删除？").then(function (_) {
        http["a" /* default */].delete("/git/repos/" + id).then(function (response) {
          _this2.$message({
            showClose: true,
            message: "删除成功",
            type: "success"
          });

          _this2.list_git_repos();
        }).catch(function (error) {
          console.log(error);

          _this2.$message.error("删除失败");
        });
      }).catch(function (_) {
        _this2.$message("已取消");
      });
    },
    updateGitRepo2Db: function updateGitRepo2Db() {
      var _this3 = this;

      this.loading = true;
      http["a" /* default */].post("/git/repos/database").then(function (response) {
        _this3.$message({
          showClose: true,
          message: "同步git信息成功",
          type: "success"
        });

        _this3.list_git_repos();
      }).catch(function (error) {
        _this3.$message.error("更新失败");
      }).then(function () {
        _this3.loading = false;
      });
    },
    list_projects_web_hooks: function list_projects_web_hooks() {
      var _this4 = this;

      this.showWebHook = true;
      this.gitRepoList.forEach(function (gitRepo) {
        http["a" /* default */].get("/git/repo/" + gitRepo.id + "/web_hooks").then(function (response) {
          gitRepo.id = gitRepo.id + ""; // 引用赋值

          gitRepo.web_hooks = JSON.stringify(response.data);
        }).catch(function (error) {
          _this4.$message.error("查询失败");
        });
      });
    },
    list_project_web_hooks: function list_project_web_hooks(row, index) {
      var _this5 = this;

      http["a" /* default */].get("/git/repo/" + row.id + "/web_hooks").then(function (response) {
        row.web_hooks = JSON.stringify(response.data);

        _this5.$set(_this5.gitRepoList, index, row);
      }).catch(function (error) {
        _this5.$message.error("查询失败");
      });
    },
    add_gitlab_web_hook: function add_gitlab_web_hook(row, index) {
      var _this6 = this;

      this.$confirm("确认添加？").then(function (_) {
        http["a" /* default */].request({
          url: "/git/repo/" + row.id + "/web_hook",
          method: "PUT",
          data: null
        }).then(function (response) {
          _this6.$message({
            showClose: true,
            message: "保存成功",
            type: "success"
          });

          _this6.list_project_web_hooks(row, index);
        }).catch(function (error) {
          _this6.$message.error("保存失败");
        });
      }).catch(function (_) {
        _this6.$message("已取消");
      });
    },
    delete_gitlab_web_hook: function delete_gitlab_web_hook(row, index) {
      var _this7 = this;

      this.$confirm("确认删除？").then(function (_) {
        http["a" /* default */].delete("/git/repo/" + row.id + "/web_hook").then(function (response) {
          _this7.$message({
            showClose: true,
            message: "删除成功",
            type: "success"
          });

          _this7.list_project_web_hooks(row, index);
        }).catch(function (error) {
          _this7.$message.error("删除失败");
        });
      }).catch(function (_) {
        _this7.$message("已取消");
      });
    }
  },
  created: function created() {
    this.list_git_repos();
  },
  mounted: function mounted() {
    var _this8 = this;

    if (this.$refs.tips) {
      setTimeout(function () {
        _this8.$refs.tips.close();
      }, 3000);
    }
  }
});
// CONCATENATED MODULE: ./src/views/GitRepoList.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_GitRepoListvue_type_script_lang_js_ = (GitRepoListvue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/GitRepoList.vue?vue&type=style&index=0&id=59c097ce&scoped=true&lang=css&
var GitRepoListvue_type_style_index_0_id_59c097ce_scoped_true_lang_css_ = __webpack_require__("2fa2");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/GitRepoList.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_GitRepoListvue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "59c097ce",
  null
  
)

/* harmony default export */ var GitRepoList = __webpack_exports__["default"] = (component.exports);

/***/ }),

/***/ "8e9a":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return cellStyle; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return cellStyleLeft; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "c", function() { return headerCellStyle; });
function cellStyle() {
  return "text-align: center;";
}

function cellStyleLeft() {
  return "text-align: left;";
}

function headerCellStyle() {
  return "text-align: center; background-color: lightgrey; height: 40px;";
}



/***/ }),

/***/ "ac6a":
/***/ (function(module, exports, __webpack_require__) {

var $iterators = __webpack_require__("cadf");
var getKeys = __webpack_require__("0d58");
var redefine = __webpack_require__("2aba");
var global = __webpack_require__("7726");
var hide = __webpack_require__("32e9");
var Iterators = __webpack_require__("84f2");
var wks = __webpack_require__("2b4c");
var ITERATOR = wks('iterator');
var TO_STRING_TAG = wks('toStringTag');
var ArrayValues = Iterators.Array;

var DOMIterables = {
  CSSRuleList: true, // TODO: Not spec compliant, should be false.
  CSSStyleDeclaration: false,
  CSSValueList: false,
  ClientRectList: false,
  DOMRectList: false,
  DOMStringList: false,
  DOMTokenList: true,
  DataTransferItemList: false,
  FileList: false,
  HTMLAllCollection: false,
  HTMLCollection: false,
  HTMLFormElement: false,
  HTMLSelectElement: false,
  MediaList: true, // TODO: Not spec compliant, should be false.
  MimeTypeArray: false,
  NamedNodeMap: false,
  NodeList: true,
  PaintRequestList: false,
  Plugin: false,
  PluginArray: false,
  SVGLengthList: false,
  SVGNumberList: false,
  SVGPathSegList: false,
  SVGPointList: false,
  SVGStringList: false,
  SVGTransformList: false,
  SourceBufferList: false,
  StyleSheetList: true, // TODO: Not spec compliant, should be false.
  TextTrackCueList: false,
  TextTrackList: false,
  TouchList: false
};

for (var collections = getKeys(DOMIterables), i = 0; i < collections.length; i++) {
  var NAME = collections[i];
  var explicit = DOMIterables[NAME];
  var Collection = global[NAME];
  var proto = Collection && Collection.prototype;
  var key;
  if (proto) {
    if (!proto[ITERATOR]) hide(proto, ITERATOR, ArrayValues);
    if (!proto[TO_STRING_TAG]) hide(proto, TO_STRING_TAG, NAME);
    Iterators[NAME] = ArrayValues;
    if (explicit) for (key in $iterators) if (!proto[key]) redefine(proto, key, $iterators[key], true);
  }
}


/***/ })

}]);
//# sourceMappingURL=chunk-40853b9e.6665494e.js.map