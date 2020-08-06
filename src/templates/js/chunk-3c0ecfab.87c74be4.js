(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-3c0ecfab"],{

/***/ "1919":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js?{"cacheDirectory":"node_modules/.cache/vue-loader","cacheIdentifier":"4bea0b5a-vue-loader-template"}!./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishList.vue?vue&type=template&id=bb66f2ac&scoped=true&
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],staticClass:"publishList"},[_c('div',{staticStyle:{"margin-bottom":"10px","width":"100%"}},[_c('el-select',{attrs:{"filterable":"","placeholder":"请选择或输入关键词","clearable":"","allow-create":"","default-first-option":""},on:{"change":function($event){return _vm.search_projects_publishment()}},model:{value:(_vm.keyword),callback:function ($$v) {_vm.keyword=$$v},expression:"keyword"}},_vm._l((_vm.keyword_options),function(item){return _c('el-option',{key:item.value,attrs:{"label":item.label,"value":item.value}})}),1),_vm._v("  \n    "),_c('el-button',{attrs:{"type":"primary"},on:{"click":function($event){return _vm.search_projects_publishment()}}},[_vm._v("搜索")]),_c('el-button',{staticStyle:{"margin-left":"120px"},attrs:{"type":"text","size":"mini","icon":"el-icon-circle-plus-outline"},on:{"click":function($event){return _vm.$router.push({path: '/newPublish'});}}},[_vm._v("新建发布")]),_c('el-button',{staticStyle:{"margin-left":"30px"},attrs:{"type":"text","plain":"","size":"mini"},on:{"click":function($event){return _vm.list_projects_health_status()}}},[_vm._v("查看健康状态")])],1),_c('el-table',{staticStyle:{"width":"100%"},attrs:{"data":_vm.publishList,"border":"","cell-style":_vm.cellStyle,"header-cell-style":_vm.headerCellStyle}},[_c('el-table-column',{attrs:{"type":"expand"},scopedSlots:_vm._u([{key:"default",fn:function(props){return [_c('el-form',{staticClass:"table-expand",attrs:{"label-position":"left","inline":""}},[_c('el-form-item',{attrs:{"label":"发布系统id"}},[_c('span',[_vm._v(_vm._s(props.row.id))])]),_c('el-form-item',{attrs:{"label":"名称"}},[_c('span',[_vm._v(_vm._s(props.row.name))])]),_c('el-form-item',{attrs:{"label":"描述"}},[_c('span',[_vm._v(_vm._s(props.row.description))])]),_c('el-form-item',{attrs:{"label":"git仓库id"}},[_c('span',[_vm._v(_vm._s(props.row.git_repo_id))])]),_c('el-form-item',{attrs:{"label":"git发布分支"}},[_c('span',[_vm._v(_vm._s(props.row.git_branches))])]),_c('el-form-item',{attrs:{"label":"maven打包环境"}},[_c('span',[_vm._v(_vm._s(props.row.profile))])]),_c('el-form-item',{attrs:{"label":"发布文件位置"}},[_c('span',[_vm._v(_vm._s(props.row.source_file_dir))])]),_c('el-form-item',{attrs:{"label":"目标服务器ip"}},[_c('span',[_vm._v(_vm._s(props.row.to_ip))])]),_c('el-form-item',{attrs:{"label":"目标服务器项目主目录"}},[_c('span',[_vm._v(_vm._s(props.row.to_project_home))])]),_c('el-form-item',{attrs:{"label":"目标服务器项目进程关键词"}},[_c('span',[_vm._v(_vm._s(props.row.to_process_name))])]),_c('el-form-item',{attrs:{"label":"目标服务器上java应用运行变量"}},[_c('span',[_vm._v(_vm._s(props.row.to_java_opts))])]),_c('el-form-item',{attrs:{"label":"git合并到的分支名"}},[_c('span',[_vm._v(_vm._s(props.row.git_merged_branch))])]),_c('el-form-item',{attrs:{"label":"git打标签名"}},[_c('span',[_vm._v(_vm._s(props.row.git_tag_version))])]),_c('el-form-item',{attrs:{"label":"git打标签备注"}},[_c('span',[_vm._v(_vm._s(props.row.git_tag_comment))])]),_c('el-form-item',{attrs:{"label":"是否删除临时分支"}},[_c('span',[_vm._v(_vm._s(props.row.git_delete_temp_branch == 1 ? '删除' : ''))])]),_c('el-form-item',{attrs:{"label":"创建时间"}},[_c('span',[_vm._v(_vm._s(props.row.created_at))])]),_c('el-form-item',{attrs:{"label":"创建人"}},[_c('span',[_vm._v(_vm._s(props.row.created_by))])]),_c('el-form-item',{attrs:{"label":"最后修改时间"}},[_c('span',[_vm._v(_vm._s(props.row.last_updated_at))])]),_c('el-form-item',{attrs:{"label":"最后修改人"}},[_c('span',[_vm._v(_vm._s(props.row.last_updated_by))])]),_c('el-form-item',{attrs:{"label":"是否删除"}},[_c('span',[_vm._v(_vm._s(props.row.is_deleted == 0 ? '正常' : '删除'))])])],1)]}}])},[_c('template',{slot:"header"},[_c('el-button',{attrs:{"type":"text","icon":"el-icon-more"}})],1)],2),_c('el-table-column',{attrs:{"width":"65","prop":"id","label":"发布id"}}),_c('el-table-column',{attrs:{"prop":"name","label":"名称"}}),_c('el-table-column',{attrs:{"prop":"description","label":"描述"}}),_c('el-table-column',{attrs:{"prop":"git_repo.path_with_namespace","label":"git仓库"}}),_c('el-table-column',{attrs:{"prop":"git_branches","label":"git发布分支"}}),_c('el-table-column',{attrs:{"prop":"profile","label":"maven打包环境"}}),_c('el-table-column',{attrs:{"prop":"to_ip","label":"目标服务器ip"}}),_c('el-table-column',{attrs:{"width":"95","label":"操作"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [_c('div',{staticStyle:{"padding-top":"2px","padding-bottom":"2px"}},[_c('el-button',{attrs:{"type":"primary","round":"","size":"mini","icon":"el-icon-edit"},on:{"click":function($event){return _vm.toUpdate(scope.row.id)}}},[_vm._v("修改")]),_c('br'),_c('el-button',{staticStyle:{"margin-top":"3px"},attrs:{"type":"danger","round":"","size":"mini","icon":"el-icon-delete"},on:{"click":function($event){return _vm.deleteItem(scope.row.id)}}},[_vm._v("删除")])],1)]}}])}),(_vm.showHealthStatus == true)?_c('el-table-column',{attrs:{"width":"80","label":"健康状态"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [(scope.row.health_status && scope.row.health_status != '')?_c('span',{staticClass:"el-icon-sunny"}):(scope.row.health_status !== undefined && scope.row.health_status == '')?_c('span',{staticClass:"el-icon-moon-night"}):_vm._e()]}}],null,false,1338655337)}):_vm._e(),_c('el-table-column',{attrs:{"label":"发布操作"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [_c('el-dropdown',{attrs:{"split-button":"","type":"primary","size":"small"},on:{"click":function($event){return _vm.toPublish(scope.row.id, scope.row.name)}}},[_c('span',{staticClass:"el-icon-s-promotion"},[_vm._v(" 发布")]),_c('el-dropdown-menu',{attrs:{"slot":"dropdown"},slot:"dropdown"},[_c('el-dropdown-item',{staticStyle:{"padding":"0 1px 2px 1px","text-align":"center"}},[_c('el-button',{attrs:{"type":"danger","plain":"","size":"mini","icon":"el-icon-close"},on:{"click":function($event){return _vm.shutdown(scope.row, scope.$index)}}},[_vm._v("停机")])],1),_c('el-dropdown-item',{staticStyle:{"padding":"2px 1px 0 1px","text-align":"center"}},[_c('el-button',{attrs:{"type":"primary","plain":"","size":"mini","icon":"el-icon-refresh"},on:{"click":function($event){return _vm.reboot(scope.row, scope.$index)}}},[_vm._v("重启")])],1)],1)],1)]}}])})],1),_c('div',{staticClass:"pagination"},[_c('el-pagination',{attrs:{"background":"","current-page":this.currentPage,"page-sizes":[10, 20, 30, 50],"page-size":this.pageSize,"layout":"total, sizes, prev, pager, next, jumper","total":this.total,"hide-on-single-page":true},on:{"size-change":_vm.change_page_size,"current-change":_vm.change_page}})],1)],1)}
var staticRenderFns = []


// CONCATENATED MODULE: ./src/views/PublishList.vue?vue&type=template&id=bb66f2ac&scoped=true&

// EXTERNAL MODULE: ./node_modules/core-js/modules/web.dom.iterable.js
var web_dom_iterable = __webpack_require__("ac6a");

// EXTERNAL MODULE: ./node_modules/core-js/modules/es6.function.name.js
var es6_function_name = __webpack_require__("7f7f");

// EXTERNAL MODULE: ./src/util/http.js
var http = __webpack_require__("adb5");

// EXTERNAL MODULE: ./src/assets/common.js
var common = __webpack_require__("8e9a");

// CONCATENATED MODULE: ./node_modules/cache-loader/dist/cjs.js??ref--12-0!./node_modules/thread-loader/dist/cjs.js!./node_modules/babel-loader/lib!./node_modules/cache-loader/dist/cjs.js??ref--0-0!./node_modules/vue-loader/lib??vue-loader-options!./src/views/PublishList.vue?vue&type=script&lang=js&


//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//


/* harmony default export */ var PublishListvue_type_script_lang_js_ = ({
  data: function data() {
    return {
      publishList: [],
      total: 0,
      currentPage: 1,
      pageSize: 10,
      keyword: null,
      loading: false,
      showHealthStatus: false,
      keyword_options: [{
        value: "youxuan",
        label: "妈妈纷享"
      }, {
        value: "pallymore",
        label: "帕力亚多学习圈"
      }, {
        value: "进货商城",
        label: "进货商城"
      }, {
        value: "pos",
        label: "店保"
      }, {
        value: "官网",
        label: "官网类"
      }, {
        value: "membergrowth",
        label: "会员增长小程序"
      }, {
        value: "hroffer",
        label: "HR公众号"
      }]
    };
  },
  methods: {
    cellStyle: function cellStyle() {
      return Object(common["a" /* cellStyle */])();
    },
    headerCellStyle: function headerCellStyle() {
      return Object(common["c" /* headerCellStyle */])();
    },
    change_page: function change_page(pageNo) {
      if (pageNo) {
        this.currentPage = pageNo;
        this.search_projects_publishment();
      }
    },
    change_page_size: function change_page_size(pageSize) {
      if (pageSize) {
        this.pageSize = pageSize;
        this.search_projects_publishment();
      }
    },
    search_projects_publishment: function search_projects_publishment() {
      var _this = this;

      http["a" /* default */].get("/publishment/list", {
        params: {
          keyword: this.keyword,
          current_page: this.currentPage,
          page_size: this.pageSize
        }
      }).then(function (response) {
        _this.publishList = response.data.data;
        _this.total = response.data.total;
      }).catch(function (error) {
        _this.$message.error("查询失败");
      });
    },
    toUpdate: function toUpdate(id) {
      this.$router.push({
        path: "/updatePublish",
        query: {
          id: id
        }
      });
    },
    deleteItem: function deleteItem(id) {
      var _this2 = this;

      this.$confirm("确认删除？").then(function (_) {
        http["a" /* default */].delete("/publishment/" + id).then(function (response) {
          _this2.$message({
            showClose: true,
            message: "删除成功",
            type: "success"
          });

          _this2.search_projects_publishment();
        }).catch(function (error) {
          _this2.$message.error("删除失败");
        });
      }).catch(function (_) {
        _this2.$message("已取消");
      });
    },
    toPublish: function toPublish(id, name) {
      this.$router.push({
        path: "/publishDetail",
        query: {
          id: id,
          name: name
        }
      });
    },
    shutdown: function shutdown(row, index) {
      var _this3 = this;

      this.$confirm("确认停机？").then(function (_) {
        _this3.$message({
          showClose: true,
          message: "正在停机，请稍等..."
        });

        http["a" /* default */].post("/publish/shutdown/" + row.id).then(function (response) {
          if (response.data.status == "OK") {
            var _h = _this3.$createElement;

            _this3.$notify({
              title: "停机状态",
              message: _h("i", {
                style: "color: green"
              }, row.name + "停机成功"),
              type: "success",
              duration: 0
            });
          } else {
            _this3.$notify.error({
              title: "停机状态",
              message: h("i", {
                style: "color: red"
              }, row.name + "停机失败，请检查异常"),
              duration: 0
            });
          }

          _this3.list_project_health_status(row, index);
        }).catch(function (error) {
          var h = _this3.$createElement;

          _this3.$notify({
            title: "停机状态",
            message: h("i", {
              style: "color: red"
            }, row.name + "停机发生异常，详情请查看相关日志"),
            type: "warning",
            duration: 0
          });
        });
      }).catch(function (_) {
        _this3.$message("已取消");
      });
    },
    reboot: function reboot(row, index) {
      var _this4 = this;

      this.$confirm("确认重启？").then(function (_) {
        _this4.$message({
          showClose: true,
          message: "正在重启，请稍等..."
        });

        http["a" /* default */].post("/publish/reboot/" + row.id).then(function (response) {
          if (response.data.status == "OK") {
            var _h2 = _this4.$createElement;

            _this4.$notify({
              title: "重启状态",
              message: _h2("i", {
                style: "color: green"
              }, row.name + "重启成功，详情请查看相关日志"),
              type: "success",
              duration: 0
            });
          } else {
            var _h3 = _this4.$createElement;

            _this4.$notify.error({
              title: "重启状态",
              message: _h3("i", {
                style: "color: red"
              }, row.name + "重启失败，详情请查看重启日志"),
              duration: 0
            });
          }

          _this4.list_project_health_status(row, index);
        }).catch(function (error) {
          var h = _this4.$createElement;

          _this4.$notify({
            title: "重启状态",
            message: h("i", {
              style: "color: red"
            }, row.name + " 重启发生异常，详情请查看相关日志"),
            type: "warning",
            duration: 0
          });
        });
      }).catch(function (_) {
        _this4.$message("已取消");
      });
    },
    list_projects_health_status: function list_projects_health_status() {
      var _this5 = this;

      this.showHealthStatus = true;
      this.publishList.forEach(function (publish) {
        http["a" /* default */].get("/publish/status/" + publish.id).then(function (response) {
          publish.id = publish.id + "";
          publish.health_status = response.data.process_id;
        }).catch(function (error) {
          _this5.$message.error("查询失败");
        });
      });
    },
    list_project_health_status: function list_project_health_status(row, index) {
      var _this6 = this;

      http["a" /* default */].get("/publish/status/" + row.id).then(function (response) {
        row.health_status = response.data.process_id;

        _this6.$set(_this6.publishList, index, row);
      }).catch(function (error) {
        _this6.$message.error("查询失败");
      });
    },
    keyupSubmit: function keyupSubmit() {
      var _this7 = this;

      document.onkeydown = function (e) {
        var _key = window.event.keyCode;

        if (_key === 13) {
          _this7.search_projects_publishment();
        }
      };
    }
  },
  created: function created() {
    this.search_projects_publishment();
    this.keyupSubmit();
  }
});
// CONCATENATED MODULE: ./src/views/PublishList.vue?vue&type=script&lang=js&
 /* harmony default export */ var views_PublishListvue_type_script_lang_js_ = (PublishListvue_type_script_lang_js_); 
// EXTERNAL MODULE: ./src/views/PublishList.vue?vue&type=style&index=0&id=bb66f2ac&scoped=true&lang=css&
var PublishListvue_type_style_index_0_id_bb66f2ac_scoped_true_lang_css_ = __webpack_require__("8a92");

// EXTERNAL MODULE: ./node_modules/vue-loader/lib/runtime/componentNormalizer.js
var componentNormalizer = __webpack_require__("2877");

// CONCATENATED MODULE: ./src/views/PublishList.vue






/* normalize component */

var component = Object(componentNormalizer["a" /* default */])(
  views_PublishListvue_type_script_lang_js_,
  render,
  staticRenderFns,
  false,
  null,
  "bb66f2ac",
  null
  
)

/* harmony default export */ var PublishList = __webpack_exports__["default"] = (component.exports);

/***/ }),

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

/***/ "8a92":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishList_vue_vue_type_style_index_0_id_bb66f2ac_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("b143");
/* harmony import */ var _node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishList_vue_vue_type_style_index_0_id_bb66f2ac_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishList_vue_vue_type_style_index_0_id_bb66f2ac_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0__);
/* unused harmony reexport * */
 /* unused harmony default export */ var _unused_webpack_default_export = (_node_modules_mini_css_extract_plugin_dist_loader_js_ref_6_oneOf_1_0_node_modules_css_loader_index_js_ref_6_oneOf_1_1_node_modules_vue_loader_lib_loaders_stylePostLoader_js_node_modules_postcss_loader_src_index_js_ref_6_oneOf_1_2_node_modules_cache_loader_dist_cjs_js_ref_0_0_node_modules_vue_loader_lib_index_js_vue_loader_options_PublishList_vue_vue_type_style_index_0_id_bb66f2ac_scoped_true_lang_css___WEBPACK_IMPORTED_MODULE_0___default.a); 

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


/***/ }),

/***/ "b143":
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ })

}]);
//# sourceMappingURL=chunk-3c0ecfab.87c74be4.js.map