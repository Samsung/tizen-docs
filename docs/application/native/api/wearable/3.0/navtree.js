var NAVTREE =
[
  [ "Tizen Native API", "index.html", [
    [ "The Basics of Tizen Native API Reference", "index.html", null ],
    [ "Native API Reference", "modules.html", "modules" ]
  ] ]
];

$(document).ready(function () {
    var current_path = window.location.pathname;
    var native_or_web = current_path.indexOf("native");
    if(native_or_web >= 0){
        native_or_web = "native";
    }else{
        native_or_web = "web";
    }
    var path = current_path.split("/");
    
    var api_platform = capitalizeFirstLetter(path[4]);
    if(api_platform != "Modile" && api_platform != "Wearable" && api_platform != "Tv") {
      api_platform = "Mobile";
    }
    var api_version = path[5];

    var div_platform = 
    '<a id="div_platform" style="border: 1px solid #d6d6d6;width: 148px;display: inline-block;padding-bottom: 10px;padding-top: 10px;text-align: center;color: #555;font-size: 16px;margin-right: 18px;" href="#nogo">'+ 
    '<span class="undefined-status" style=" width: 100px;left: left;font-size: 100%;font-weight: 400;">' + api_platform + '</span>' +
    '<span id="platformIcon" class="undefined-icon" style="    width: 16px;    background: url(/images/form-select_type1.png) no-repeat 50%;    height: 16px;    float: right;    margin-right: 11px;    margin-top: 3px;"></span>' +
    '</a>';
    
    var div_verion = 
    '<a id="div_verion" style="border: 1px solid #d6d6d6;width: 148px;display: inline-block;padding-top: 10px;padding-bottom: 10px;text-align: center;color: #555;font-size: 16px;" href="#nogo">' +
    '<span class="undefined-status" style=" width: 100px;left: left;font-size: 100%;font-weight: 400;">' + api_version + '</span>' +
    '<span id="versionIcon" class="undefined-icon" style="    width: 16px;    background: url(/images/form-select_type1.png) no-repeat 50%;    height: 16px;    float: right;    margin-right: 11px;    margin-top: 3px;"></span>' +
    '</a>';

    var div_common = '<div style="margin-top: 16px; margin-bottom: 10px; margin-left: 30px;">' + div_platform + div_verion + '</div>';
    $('#nav-tree').prepend(div_common);
    
    var div_search = '<div class="flexbox"><div class="flex1"></div><div class="tizen-search-api" style="float: right;"><form id="form-search-api"><div class="form-group-search"><input type="text" placeholder="Search related API References" name="search-api" id="search-api" style="padding-right: 38px !important;"><button class="btn btn-submit" id="btn-search-api"><svg width="32" height="32" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1216 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z"></path></svg></button></div></form></div></div>';
    $('#doc-content').prepend(div_search);
    
    var btGotoTop = '<div><input type="image" id="btngototop" src="/images/btn_go_to_top.png" style="display: none"></div>';
    $('body').append(btGotoTop);
    
    var btnTop = $('#btngototop');
    $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
          btnTop.show();
        } else {
          btnTop.hide();
        }
    });
    btnTop.click(function () {
        $('html, body').animate({scrollTop:0}, '300');
    });
    
    $('#btn-search-api').click(function (event) {
        event.preventDefault();
        var search_text = $('#search-api').val();
        var current_url = window.location.href;
        var current_url_array = current_url.split("/");
        var to_url = '';
        for(var i=0; i< current_url_array.length -1; i++){
            to_url += current_url_array[i] + "/";
        }
        to_url += 'search-api-reference.php?search=' + search_text;
        window.location.href = to_url;
    });
    
    var navbar_header = 
    '<div class="navbar-wrapper">' +
        '<nav class="navbar navbar-default navbar-static-top navbar-fixed-top">' +
             '<div class="container">' +
                '<div class="navbar-header">' +
                    '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar">' +
                        '<span class="sr-only">Toggle navigation</span>' +
                        '<span class="icon-bar"></span>' +
                        '<span class="icon-bar"></span>' +
                        '<span class="icon-bar"></span>' +
                    '</button>' +
                    '<a class="navbar-brand" href="/">' +
                        '<span class="brand-tizen"><img src="/images/logo.png" alt="logo"></span>' +
                        '<span class="brand-docs">Docs</span>' +
                    '</a>' +
                '</div>' +

                '<ul id="navbar" class="nav navbar-nav navbar-right">' +
                    '<li><a href="/platform/about/tizen-open-source-overview">Platform</a></li>' +
                    '<li><a href="/application/">Application</a></li>' +
                    '<li><a href="/iot/">IoT</a></li>' +
                    '<li><a href="https://developer.tizen.org/development/tizen-studio/download" target="_blank">Download</a></li>' +
                    '<li class="navbar-divisor"></li>' +

                    '<li class="search"><a id="gnb_search_btn" href="#"><div class="search-btn"></div></a>' +
                      '<form method="GET" id="gnb_search_box" class="searchbox" action="/search.php">' +
                        '<input class="form-control" type=text name="q" placeholder="Search ...">' +
                        '<a href="#"><img src="/images/ic_search_ac.png"></a>' +
                      '</form>' +
                    '</li>' +
                '</ul>' +

            '</div>' +
        '</nav>' +
    '</div>';
    
    $("body").prepend(navbar_header);
    
    var api_platform_version = {"api_platform": api_platform, "api_version": api_version, "native_or_web": native_or_web};
    $.ajax({
        type: "POST",
        url: '/api/api-reference-navtree-contents.php',
        data: api_platform_version,
        dataType: "text",
        success: function(response){
            $('#nav-tree-contents').html(response);
            var menujsElement = document.createElement("script");
            menujsElement.src = "/js/menu.js";
            menujsElement.type = "text/javascript";
            document.getElementsByTagName("head")[0].appendChild(menujsElement);
        }
   });      
    
    register_gnb_search_btn();
});
function register_gnb_search_btn() {
  $('#gnb_search_btn').click(function() {
    $('#gnb_search_box').fadeIn(500);
    $('#gnb_search_box > input').focus();
  });

  $('#gnb_search_box > input').blur(function() {
    $('#gnb_search_box').fadeOut(500);
  });
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function getData(varName)
{
  var i = varName.lastIndexOf('/');
  var n = i>=0 ? varName.substring(i+1) : varName;
  return eval(n);
}

function stripPath(uri)
{
  return uri.substring(uri.lastIndexOf('/')+1);
}

function getScript(scriptName,func,show)
{
  var head = document.getElementsByTagName("head")[0]; 
  var script = document.createElement('script');
  script.id = scriptName;
  script.type = 'text/javascript';
  script.onload = func; 
  script.src = scriptName+'.js'; 
  script.onreadystatechange = function() {
    if (script.readyState == 'complete') { func(); if (show) showRoot(); }
  };
  head.appendChild(script); 
}

function createIndent(o,domNode,node,level)
{
  if (node.parentNode && node.parentNode.parentNode)
  {
    createIndent(o,domNode,node.parentNode,level+1);
  }
  var imgNode = document.createElement("img");
  imgNode.width = 16;
  imgNode.height = 22;
  if (level==0 && node.childrenData)
  {
    node.plus_img = imgNode;
    node.expandToggle = document.createElement("a");
    node.expandToggle.href = "javascript:void(0)";
    node.expandToggle.onclick = function() 
    {
      if (node.expanded) 
      {
        $(node.getChildrenUL()).slideUp("fast");
        if (node.isLast)
        {
          node.plus_img.src = node.relpath+"ftv2plastnode.png";
        }
        else
        {
          node.plus_img.src = node.relpath+"ftv2pnode.png";
        }
        node.expanded = false;
      } 
      else 
      {
        expandNode(o, node, false, false);
      }
    }
    node.expandToggle.appendChild(imgNode);
    domNode.appendChild(node.expandToggle);
  }
  else
  {
    domNode.appendChild(imgNode);
  }
  if (level==0)
  {
    if (node.isLast)
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2plastnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2lastnode.png";
        domNode.appendChild(imgNode);
      }
    }
    else
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2pnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2node.png";
        domNode.appendChild(imgNode);
      }
    }
  }
  else
  {
    if (node.isLast)
    {
      imgNode.src = node.relpath+"ftv2blank.png";
    }
    else
    {
      imgNode.src = node.relpath+"ftv2vertline.png";
    }
  }
  imgNode.border = "0";
}

function newNode(o, po, text, link, childrenData, lastNode)
{
  var node = new Object();
  node.children = Array();
  node.childrenData = childrenData;
  node.depth = po.depth + 1;
  node.relpath = po.relpath;
  node.isLast = lastNode;

  node.li = document.createElement("li");
  po.getChildrenUL().appendChild(node.li);
  node.parentNode = po;

  node.itemDiv = document.createElement("div");
  node.itemDiv.className = "item";

  node.labelSpan = document.createElement("span");
  node.labelSpan.className = "label";

  createIndent(o,node.itemDiv,node,0);
  node.itemDiv.appendChild(node.labelSpan);
  node.li.appendChild(node.itemDiv);

  var a = document.createElement("a");
  node.labelSpan.appendChild(a);
  node.label = document.createTextNode(text);
  node.expanded = false;
  a.appendChild(node.label);
  if (link) 
  {
    a.className = stripPath(link.replace('#',':'));
    if (link.indexOf('#')!=-1)
    {
      var aname = '#'+link.split('#')[1];
      var srcPage = stripPath($(location).attr('pathname'));
      var targetPage = stripPath(link.split('#')[0]);
      a.href = srcPage!=targetPage ? node.relpath+link : '#';
      a.onclick = function(){
        $('.item').removeClass('selected');
        $('.item').removeAttr('id');
        $(a).parent().parent().addClass('selected');
        $(a).parent().parent().attr('id','selected');
        var anchor = $(aname);
        $("#doc-content").animate({
          scrollTop: anchor.position().top +
          $('#doc-content').scrollTop() -
          $('#doc-content').offset().top
        },500,function(){
          window.location.replace(aname);
        });
      };
    }
    else
    {
      a.href = node.relpath+link;
    }
  } 
  else 
  {
    if (childrenData != null) 
    {
      a.className = "nolink";
      a.href = "javascript:void(0)";
      a.onclick = node.expandToggle.onclick;
    }
  }

  node.childrenUL = null;
  node.getChildrenUL = function() 
  {
    if (!node.childrenUL) 
    {
      node.childrenUL = document.createElement("ul");
      node.childrenUL.className = "children_ul";
      node.childrenUL.style.display = "none";
      node.li.appendChild(node.childrenUL);
    }
    return node.childrenUL;
  };

  return node;
}

function showRoot()
{
  var headerHeight = $("#top").height();
  var footerHeight = $("#nav-path").height();
  var windowHeight = $(window).height() - headerHeight - footerHeight;
  (function (){ // retry until we can scroll to the selected item
    try {
      navtree.scrollTo('#selected',0,{offset:-windowHeight/2});
    } catch (err) {
      setTimeout(arguments.callee, 0);
    }
  })();
}

function expandNode(o, node, imm, showRoot)
{
  if (node.childrenData && !node.expanded) 
  {
    if (typeof(node.childrenData)==='string')
    {
      var varName    = node.childrenData;
      getScript(node.relpath+varName,function(){
        node.childrenData = getData(varName);
        expandNode(o, node, imm, showRoot);
      }, showRoot);
    }
    else
    {
      if (!node.childrenVisited) 
      {
        getNode(o, node);
      }
      if (imm)
      {
        $(node.getChildrenUL()).show();
      } 
      else 
      {
        $(node.getChildrenUL()).slideDown("fast");
      }
      if (node.isLast)
      {
        node.plus_img.src = node.relpath+"ftv2mlastnode.png";
      }
      else
      {
        node.plus_img.src = node.relpath+"ftv2mnode.png";
      }
      node.expanded = true;
    }
  }
}

function showNode(o, node, index)
{
  if (node.childrenData && !node.expanded) 
  {
    if (typeof(node.childrenData)==='string')
    {
      var varName    = node.childrenData;
      getScript(node.relpath+varName,function(){
        node.childrenData = getData(varName);
        showNode(o,node,index);
      },true);
    }
    else
    {
      if (!node.childrenVisited) 
      {
        getNode(o, node);
      }
      $(node.getChildrenUL()).show();
      if (node.isLast)
      {
        node.plus_img.src = node.relpath+"ftv2mlastnode.png";
      }
      else
      {
        node.plus_img.src = node.relpath+"ftv2mnode.png";
      }
      node.expanded = true;
      var n = node.children[o.breadcrumbs[index]];
      if (index+1<o.breadcrumbs.length)
      {
        showNode(o,n,index+1);
      }
      else
      {
        if (typeof(n.childrenData)==='string')
        {
          var varName = n.childrenData;
          getScript(n.relpath+varName,function(){
            n.childrenData = getData(varName);
            node.expanded=false;
            showNode(o,node,index); // retry with child node expanded
          },true);
        }
        else
        {
          if (o.toroot=="index.html" || n.childrenData)
          {
            expandNode(o, n, true, true);
          }
          var a;
          if ($(location).attr('hash'))
          {
            var link=stripPath($(location).attr('pathname'))+':'+
                     $(location).attr('hash').substring(1);
            a=$('.item a[class*=\""'+link+'"\"]');
          }
          if (a && a.length)
          {
            a.parent().parent().addClass('selected');
            a.parent().parent().attr('id','selected');
            var anchor = $($(location).attr('hash'));
            var targetDiv = anchor.next();
            $(targetDiv).children('.memproto,.memdoc').
                     effect("highlight", {}, 1500);
          }
          else
          {
            $(n.itemDiv).addClass('selected');
            $(n.itemDiv).attr('id','selected');
          }
        }
      }
    }
  }
}

function getNode(o, po)
{
  po.childrenVisited = true;
  var l = po.childrenData.length-1;
  for (var i in po.childrenData) 
  {
    var nodeData = po.childrenData[i];
    po.children[i] = newNode(o, po, nodeData[0], nodeData[1], nodeData[2],
      i==l);
  }
}

//function initNavTree(toroot,relpath)
//{
//  var o = new Object();
//  o.toroot = toroot;
//  o.node = new Object();
//  o.node.li = document.getElementById("nav-tree-contents");
//  o.node.childrenData = NAVTREE;
//  o.node.children = new Array();
//  o.node.childrenUL = document.createElement("ul");
//  o.node.getChildrenUL = function() { return o.node.childrenUL; };
//  o.node.li.appendChild(o.node.childrenUL);
//  o.node.depth = 0;
//  o.node.relpath = relpath;
//  o.node.expanded = false;
//  o.node.isLast = true;
//  o.node.plus_img = document.createElement("img");
//  o.node.plus_img.src = relpath+"ftv2pnode.png";
//  o.node.plus_img.width = 16;
//  o.node.plus_img.height = 22;
//
//  getScript(relpath+"navtreeindex",function(){
//    var navTreeIndex = eval('NAVTREEINDEX');
//    if (navTreeIndex) {
//      o.breadcrumbs = navTreeIndex[toroot];
//      if (o.breadcrumbs==null) o.breadcrumbs = navTreeIndex["index.html"];
//      o.breadcrumbs.unshift(0);
//      showNode(o, o.node, 0);
//    }
//  },true);
//
//  $(window).bind('hashchange', function(){
//     if (window.location.hash && window.location.hash.length>1){
//       var anchor = $(window.location.hash);
//       var targetDiv = anchor.next();
//       $(targetDiv).children('.memproto,.memdoc').effect("highlight",{},1500);
//       var docContent = $('#doc-content');
//       if (docContent && anchor && anchor[0] && anchor[0].ownerDocument){
//         docContent.scrollTop(anchor.position().top+docContent.scrollTop()-docContent.offset().top);
//       }
//       var a;
//       if ($(location).attr('hash')){
//         var link=stripPath($(location).attr('pathname'))+':'+
//                  $(location).attr('hash').substring(1);
//         a=$('.item a[class*=\""'+link+'"\"]');
//       }
//       if (a && a.length){
//         $('.item').removeClass('selected');
//         $('.item').removeAttr('id');
//         a.parent().parent().addClass('selected');
//         a.parent().parent().attr('id','selected');
//         var anchor = $($(location).attr('hash'));
//         var targetDiv = anchor.next();
//         showRoot();
//       }
//     } else {
//       var docContent = $('#doc-content');
//       if (docContent){ docContent.scrollTop(0); }
//     }
//  })
//
//  $(window).load(showRoot);
//}
