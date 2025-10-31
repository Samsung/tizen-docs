// /////////////////////////////////////////////////////////////////////////////////////////////////
// # com.samsung.devloper common core javascript #
// # Create Date : 2012.07.10. 
// # Create By : kangki
;(function ($) {
/**
 * Samsung Developer Common JavaScript
 */
$.SD = {};

/*
 * Method Common
 */
$.SD.message = function (msg) { if (msg) alert(msg); };
$.SD.replaceAll = function (str, from, to) { return str.split(from).join(to); }
$.SD.typeOf = function (data) { var func = func || Object.prototype.toString; return func.call(data); };
$.SD.typeTest = function (data, datatype) {
	if (datatype === "String" || datatype === "string") return /String/.test($.SD.typeOf(data));
	if (datatype === "Number" || datatype === "number") return /Number/.test($.SD.typeOf(data));
	if (datatype === "Array" || datatype === "array") return /Array/.test($.SD.typeOf(data));
	if (datatype === "Boolean" || datatype === "boolean") return /Boolean/.test($.SD.typeOf(data));
	if (datatype === "Function" || datatype === "function") return /Function/.test($.SD.typeOf(data));
	if (datatype === "Date" || datatype === "date") return /Date/.test($.SD.typeOf(data));
	if (datatype === "Object" || datatype === "object") return /Object/.test($.SD.typeOf(data));

	return (new RegExp("/" + datatype + "/")).test($.SD.typeOf(data));
};

$.SD.toDate = function (date, seperator) {
	if (!seperator) seperator = '-';

	date = $.SD.replaceAll(date, seperator, '');
	date = $.SD.replaceAll(date, '/', '');

	if (date.length !== 8) return null;
	
	date = new Date(date.substring(0,4) + '/' + date.substring(4,6) + '/' + date.substring(6,8));

	if (date.valueOf().toString() === 'NaN') return null;

	return date;
};

$.SD.toDateString = function (date, seperator) {
	if (!seperator) seperator = '/';
	if (/String/.test(Object.prototype.toString.call(date))) date = $.SD.toDate(date);
	if (/Date/.test(Object.prototype.toString.call(date)) === false) return "";

	var str, dateString = date.getFullYear();

	str 		= "0" + (date.getMonth()+1);
	dateString 	= dateString + seperator + str.substring(str.length-2, str.length);
	str 		= "0" + date.getDate();
	dateString 	= dateString + seperator + str.substring(str.length-2, str.length);

	return dateString;
};

$.SD.addYear = function (date, number) { date.setYear(date.getFullYear() + number); return date; };
$.SD.addMonth = function (date, number) { date.setMonth(date.getMonth() + number); return date; };
$.SD.addDate = function (date, number) { date.setDate(date.getDate() + number); return date; };

$.SD.insertComma = function(num) {
	var tnum    = num + "";
	var tarr    = new Array();
	var dot     = "";
	var idxDot  = tnum.indexOf(".");
	var sign    = "";
	var tinx    = 0;
	var fnum    = tnum;
	 
	
	if(idxDot > -1) {
		fnum = tnum.substring(0, idxDot);
		dot  = tnum.substring(idxDot);
		tnum = fnum;
	} 
	
	if(tnum.indexOf("-") > -1) {
		fnum = tnum.substring(1);
		sign = tnum.substring(0, 1);
	}
	
	for(var inx = fnum.length; inx > 0; ) {
		tarr[tinx++] = fnum.substring(inx, inx - 3);
		inx = inx - 3;
	}
	
	return sign + tarr.reverse().join(",") + dot;
}

/**
 * Method Ajax
 */
$.SD.ajax = {
	doAjax : function (json) {
		var param = {
			async : json.async,
			type : json.type,
			dataType : json.dataType,
			cache: json.cache,
			timeout : json.timeout,
			success : json.success,
			error : json.error
		};

		if (param.dataType === 'jsonp') {
			param.url = json.url + '?' + $.param(json.data) + '&callback=?';
		} else {
			param.url = json.url;
			param.data = json.data;
		}
		$.ajax(param);
	},
	
	get : function (json) {
		$.SD.ajax.doAjax({ 
			url:json.url,
			cache:json.cache != null ? json.cache : false,
			async:json.async != null ? json.async : true,
			type:'get', 
			dataType:'json',
			data:json.data != null ? json.data : {}, 
			timeout:10000, success:json.success, 
			error: function(){ if(json.error != null)json.error(); }
		});
	},
	
	post : function (json) {
		$.SD.ajax.doAjax({ url:json.url,
			cache: json.cache != null ? json.cache : false,
			async:json.async != null ? json.async : true,
			type:'post', dataType:'json',
			data:json.data != null ? json.data : {}, 
			timeout:10000, success:json.success, 
			error: function(){ if(json.error != null)json.error(); }
		});
	}
};

/**
 * SD20 password check
 */

$.SD.isSD20Pwd = function(pwd) {
	
	if(/[a-zA-Z]{1,}/.test(pwd) == false) {
		return false;
	}
	
	if(/[0-9]{1,}/.test(pwd) == false) {
		return false;
	}
	
	if(/^[0-9a-zA-Z]{6,16}$/.test(pwd) == false) {
		return false;
	}
	
	return true;
};

$.SD.popupCenter = function(popObj) {
	var scrollbars  = "no";
	var resizeable  = "no";
	
	if(popObj.scrollbars) {
		scrollbars = popObj.scrollbars; 
	}
	
	if(popObj.resizeable) {
		resizeable = popObj.resizeable;
	}
	
	var width  = screen.width;
	var height = screen.height;

	var x = ( width / 2 ) - ( popObj.width / 2 );
	var y = ( height / 2 ) - ( popObj.height / 2 );

	var opt = "left=" + x +
	          ",top=" + y +
	          ",width=" + popObj.width +
	          ",height=" + popObj.height +
	          ",toolbar=no,location=no,directories=no,status=no,menubar=no" +
	          ",scrollbars=" + scrollbars +
	          ",resizable=" + resizeable;
	var pop = window.open(popObj.url, popObj.target, opt);
	if(pop) {
		pop.focus();
	}
}

$.SD.isValidDate = function(val) {
	if(val.length != 8) {
		return false;
	}
	
	var yyyy = Number(val.substring(0, 4)); 
	var mm   = Number(val.substring(4, 6));
	var dd   = Number(val.substring(6));
	
	if( mm < 1 || mm > 12 ) {
		return false;
	}
	
	var endDay  = 0;
	
	if( mm == 2 ) {
		if(yyyy % 4 == 0 && yyyy % 100 != 0 || yyyy % 400 == 0) {
			endDay = 29;
		} else {
			endDay = 28;
		}
		
	} else {
		var endDays = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
		endDay = endDays[mm - 1];
	}
	
	if( dd <= 0 || dd > endDay ) {
		return false;
	} 
	
	return true;
	
}

$.SD.boardDownload = function(option, func) {
	var jsonData = {
		url: "/board/ajaxDwnldProc.do",
		async: false,
		data: {ctgy1: option.ctgy1, ctgy2: option.ctgy2, ctgyId: option.ctgyId, bdId: option.bdId, attachId: option.attachId},
		success: function(data) {
			if(data.existFileYn == "Y") {
				location.href = "/board/download.do?bdId=" + option.bdId + "&attachId=" + option.attachId;
				//location.href = $(obj).attr("href");
				if(func) {
					func(data);
				}	
			} else {
				alert("File does not exist.");
			}
		}
	}
	
	$.SD.ajax.get(jsonData);
}

$.SD.commonDownload = function(fileName, categoryId, func) {
	var jsonData = {
		url: "/common/ajaxCommonDwnldProc.do",
		async: false,
		data: {fileName: fileName, categoryId: categoryId},
		success: function(data) {
			if(data.existFileYn == "Y") {
				location.href = "/common/commonDownload.do?fileName=" + fileName + "&categoryId=" + categoryId;
				if(func) {
					func(data);
				}	
			} else {
				alert("File does not exist.");
			}
		}
	}
	
	$.SD.ajax.get(jsonData); 
}

$.SD.commonDownloadLog = function(fileFullPath, categoryId, func) {
	var jsonData = {
		url: "/common/ajaxCommonDownloadLogProc.do",
		async: false,
		data: {fileFullPath: fileFullPath, categoryId: categoryId},
		success: function(data) {
			if(data.existFileYn == "Y") {
				//location.href = "/common/commonDownload.do?fileName=" + fileName + "&categoryId=" + categoryId;
				location.href = fileFullPath;
				if(func) {
					func(data);
				}	
			} else {
				alert("File does not exist.");
			}
		}
	}
	
	$.SD.ajax.get(jsonData); 
}

$.SD.commonDownloadLogTarget = function(fileFullPath, categoryId, target, func) {
	var jsonData = {
		url: "/common/ajaxCommonDownloadLogProc.do",
		async: false,
		data: {fileFullPath: fileFullPath, categoryId: categoryId},
		success: function(data) {
			if(data.existFileYn == "Y") {
				//location.href = "/common/commonDownload.do?fileName=" + fileName + "&categoryId=" + categoryId;
				if(target == 'new'){
					window.open(fileFullPath, '');
				}else{
					location.href = fileFullPath;
				}
				
				if(func) {
					func(data);
				}	
			} else {
				alert("File does not exist.");
			}
		}
	}
	
	$.SD.ajax.get(jsonData); 
}

$.SD.commonAllShareClickCount = function(fileFullPath, categoryId, func) {
	var jsonData = {
		url: "/common/ajaxCommonAllShareClickCountProc.do",
		async: false,
		data: {fileFullPath: fileFullPath, categoryId: categoryId},
		success: function(data) {}
	}
	
	$.SD.ajax.get(jsonData); 
}

$.SD.commonClickCount = function(categoryName, categoryId) {
	var jsonData = {
		url: "/common/ajaxCommonClickCountProc.do",
		data: {categoryName: categoryName, categoryId: categoryId},
		success: function(data) {}
	}
	
	$.SD.ajax.get(jsonData);
}

$.SD.getByteLen = function(str) {
	var resultSize = 0;
	if(str == null){
		return 0;
	}
	for(var i=0; i<str.length; i++){
	  var c = escape(str.charAt(i));
	  if(c.length == 1){
		  resultSize ++;
	  }	else if(c.indexOf("%u") != -1) {
		  resultSize += 2;
	  }	else if(c.indexOf("%") != -1) {
		  resultSize += c.length/3;
	  }
	}
	return resultSize;
}

$.SD.cutByte = function(str, limit) {
	var tempStr = new String(str);
	var len = 0;
	for ( var i = 0; i < str.length; i++) {
		var c = escape(str.charAt(i));
		if (c.length == 1)
			len++;
		else if (c.indexOf("%u") != -1)
			len += 2;
		else if (c.indexOf("%") != -1)
			len += c.length / 3;
		if (len > limit) {
			tempStr = tempStr.substring(0, i);
			break;
		}
	}
	return tempStr;
}

$.SD.pagination = {alt:{first:"",prev:"",next:"",last:""}};

/* ---------------- ADD JQUERY CUSTOM METHOD -------------------------------- */

/** 
 * Method pagination 
 * */
$.fn.frontPagination = function (pageInfo, func) {
	var info = {
			 prev : 1
			,first : 1
			,begin : pageInfo.begin - 0
			,current : pageInfo.current - 0
			,end : pageInfo.end - 0
			,last : pageInfo.last - 0
			,next : 1
		},
		target 	= this, 
		page 	= $('<span class="page"></span>'),
		prev 	= "", 
		next 	= "", 
		i 		= 0, 
		n 		= 0;

	info.begin 	 = info.begin < 1 ? 1 : info.begin;
	info.current = info.current < 1 ? 1 : info.current;
	info.end 	 = info.end < 1 ? 1 : info.end;
	info.last 	 = info.last < 1 ? 1 : info.last;

	info.prev = info.current - 1;
	info.next = info.current + 1;

	target.addClass("pageNumber");
	target.addClass("mt20");
	target.children().remove();

	if (info.first < info.begin) {
		target.append($('<a href="#" class="first"><img src="/images/common/ico/ico_arr_first.gif" alt="'+$.SD.pagination.alt.first+'" /></a>').bind('click', function(e) {
			e.preventDefault();
			func(info.first);
		}));
	}

	if (info.prev >= info.first) {
		target.append($('<a href="#" class="prev"><img src="/images/common/ico/ico_arr_prev.gif" alt="'+$.SD.pagination.alt.prev+'"/></a>').bind('click', function(e) {
			e.preventDefault();
			func(info.prev);
		}));
	}

	i = info.begin;
	n = info.end;
	for(; i <= n; i++) {
		if (i === info.current) {
			page.append('<strong>'+i+'</strong>');
		} else {
			(function(index){
				page.append($('<a href="#">'+index+'</a>').bind('click', function(e){
					e.preventDefault();
					func(index);
				}));
			})(i);
		}
	}

	target.append(page);

	if (info.next <= info.last) {
		target.append($('<a href="#" class="next"><img src="/images/common/ico/ico_arr_next.gif" alt="'+$.SD.pagination.alt.next+'" /></a>').bind('click', function(e) {
			e.preventDefault();
			func(info.next);
		}));
	}
	
	if (info.last > info.end) {
		target.append($('<a href="#" class="last"><img src="/images/common/ico/ico_arr_last.gif" alt="'+$.SD.pagination.alt.last+'" /></a>').bind('click', function(e) {
			e.preventDefault();
			func(info.last);
		}));
	}	
};

/**
 *  Method : popup Show Hide 
 */
$.fn.popupShow = function(options) {
	var opts = $.extend({}, $.fn.popupShow.defaults, options);
	
	if($("body div#" + opts.maskId).size() == 0) {
		$("body").append("<div id='" + opts.maskId + "'></div>");
		$("#" + opts.maskId).css({
			"position" : "absolute",
			"left"     : "0",
			"top"      : "0",
			"z-index"  : "9000",
			"background-color" : "#000",
			"display"  : "none"
		});
	}
	
	var mask_layer  = $("#" + opts.maskId);
	var popup_layer = $(this);
	
	popup_layer.css("z-index", "9999");
	
	var maskHeight = $(document).height();
	var maskWidth = $(window).width();
	
	mask_layer.css({'width':maskWidth,'height':maskHeight});
	
	mask_layer.fadeIn(opts.fadeSec);
	mask_layer.fadeTo(opts.speed, opts.fadeLow);
	
	var winH = $(window).height();
	var winW = $(window).width();
	
	popup_layer.css('top',  $(window).scrollTop() + winH/2 - popup_layer.height()/2);
	popup_layer.css('left', $(window).scrollLeft()  + winW/2 - popup_layer.width()/2);
	
	popup_layer.fadeIn(opts.fadeSec);
	
	var init_num = 0;
	
	if(init_num == 0) {
		mask_layer.click(function() {
			$(this).hide();
			popup_layer.hide();
		});
		
		
		$("#" + opts.closeId).click( function(e) {
			e.preventDefault();
			popup_layer.popupHidden(opts.maskId);
		});
		
		
		$(window).resize( function() {
			var maskHeight = $(document).height();
			var maskWidth  = $(window).width();
			var winH       = $(window).height();
			var winW       = $(window).width();
			
			mask_layer.css({'width':maskWidth,'height':maskHeight});
			
			popup_layer.css('top',  $(window).scrollTop() + winH/2 - popup_layer.height()/2);
			popup_layer.css('left', $(window).scrollLeft()  + winW/2 - popup_layer.width()/2);
		});
		
		init_num++;
	}
};

$.fn.popupHidden = function(maskId) {
	var id = "#";
	
	if(maskId) {
		id = id + maskId;
	} else {
		id = id + $.fn.popupShow.defaults.maskId; 
	}
	
	$(id).hide();
	$(this).hide();
};


$.fn.popupShow.defaults = {
	speed : "slow",
	fadeLow : 0.8,
	fadeSec : 100,
	maskId  : "mask",
	popupId : "layer-pop",
	closeId : "layer-pop-close"
};

/**
 *  Method : validate File Ext
 */
$.fn.isNotValidateFileExt = function(imgExts) {
	imgExts = imgExts || {txt:true, xls:true, xlsx:true, doc:true, docx:true, ppt:true, pptx:true, pdf:true, bmp:true,gif:true, jpeg:true, jpg:true, png:true, zip:true, swf:true};
	var that = this;
	var target = null;

	that.each(function (i, item) {
		var filePath = $(item).attr('type') === 'file' ? $(item).val() : '';
		if (filePath != "") {
			var fileExt  = filePath.substring(filePath.lastIndexOf(".") + 1).toLowerCase();
			if (!imgExts[fileExt]) {
				target = item;
				return false;
			}
		}
	});

	return target;
}	

/**
 *  Method : validate SD20 Password
 */
$.validator.addMethod("isSD20Pwd", function(value, element) {
	return this.optional(element) 
	       || $.SD.isSD20Pwd(value);
}, "비밀번호를 다시 입력해 주세요.");

$.SD.alterParent = function(options, event) {
    var label = $(this).data('label');
    
    /*
    if (event && event.type === 'focusin') {
      label.hide();
    } else if (event && event.type === 'focusout') {
      label.css('opacity', options.placeholderOpacity);
    }
    */
    
    if (event && event.type !== 'keydown') {
      toggleLabel(this, label);
    } else {
      // Use timeout to catch val() just after the key is pressed
      // Using keyup is too slow.   
      (function(input) {
        setTimeout(function() {
          toggleLabel(input, label);
        }, 0);
      })(this);
    }
    
    if (event && event.type === 'focusin') {
    	label.hide();
    }
  };
  
  var toggleLabel = function(input, label) {
    if ($(input).val()) {
      label.hide();
    } else {
      label.show();
    }
  };

  $.fn.stickyPlaceholders = function(options) {
    var defaults = {
      wrapperClass: 'sticky-placeholder-wrapper',
      wrapperDisplay: 'block',
      labelClass: 'sticky-placeholder-label',
      placeholderAttr: 'placeholder',
      dataAttr: 'data-sticky-placeholder',
      placeholderColor: '#000',
      placeholderOpacity: 0.5,
      placeholderFocusOpacity: 0.25
    };
    options = $.extend(defaults, options);

    return this.each(function() {
      var input       = $(this),
          placeholder = input.attr(options.placeholderAttr),
          wrapper     = $(this).wrap('<span class="' + options.wrapperClass + '" />').parent().css({'position':'relative', 'display':options.wrapperDisplay}),
          label       = $('<label class="' + options.labelClass + '" for="' + input.attr('id') + '">' + placeholder + '</label>').appendTo(wrapper),
          labelStyle;

      // store a reference to each input's label
      input.data('label', label);

      // remove the placeholder attribute to avoid conflcits
      input.removeAttr('placeholder');
      
      // If the dataAttr is set and it's not equal to the placeholderAttr
      if ( options.dataAttr && options.placeholderAttr !== options.dataAttr ) {
        input.attr('data-sticky-placeholder', placeholder);
      }

      labelStyle = {
        'color': options.placeholderColor,
        'cursor': 'text',
        'font-family': input.css('font-family'),
        'font-weight': input.css('font-weight'),
        'font-size': input.css('font-size'),
        'left': parseInt(input.css('border-left-width'), 10) + parseInt(input.css('margin-left'), 10),
        'line-height': this.currentStyle ? this.currentStyle.lineHeight : input.css('line-height'),
        // fix for an IE/jQuery bug returning 1px when the line-height doesn't have a unit: http://bugs.jquery.com/ticket/2671
        'opacity': options.placeholderOpacity,
        'padding-left': input.css('padding-left'),
        'padding-top': input.css('padding-top'),
        'position': 'absolute',
        'text-transform': input.css('text-transform'),
        'top': parseInt(input.css('border-top-width'), 10) + parseInt(input.css('margin-top'), 10)
      };
      label.css(labelStyle);
      
      // hide the placeholder if the input already has a value
      if (input.val()) {
        label.hide();
      }

      $(this).bind('keydown input focusin focusout', function(event) {
        $.SD.alterParent.call(this, options, event);
      });
        
      // prevent click/dblclick from selecting the label text
      label.bind('mousedown', function(e) {
        e.preventDefault();
      });
      
      // call alterParent initially without an event to set up the wrapper elements
      $.SD.alterParent.call(this, options);
    });
  };
 
$.SD.setInputFileKeyEvent = function(file_id, after_id) {
	$("#" + file_id).on("keydown", function(e) {
		var that = $(this);
		if(e.which == 9 && e.shiftKey) {
			return true;
		}
		
		if(e.which === 9) {
			e.preventDefault();
			setTimeout(function() {
				$("#" + after_id).focus();
			}, 1);
		}
	});
	
	$("#" + after_id).on("keydown", function(e) {
		if(e.which == 9 && e.shiftKey) {
			e.preventDefault();
			setTimeout(function() {
				$("#" + file_id).focus();
			}, 1);
		}
	});
}  

$.SD.closeWP = function() {
	var Browser = navigator.appName;
	var indexB = Browser.indexOf('Explorer');
	if (indexB > 0) {
	    var indexV = navigator.userAgent.indexOf('MSIE') + 5;
	    var Version = navigator.userAgent.substring(indexV, indexV + 1);
	    window.opener.focus();
	    if (Version >= 7) {
	        window.open('', '_self', '');
	        window.close();
	    }
	    else if (Version == 6) {
	        window.opener = null;
	        window.close();
	    }
	    else {
	        window.opener = '';
	        window.close();
	    }
	}
	else {
	    window.close();
	}
}

$.SD.profileFacebook = function() {
	location.replace("http://facebook.com/profile.php");
}

/* ------------------------------ END --------------------------------------- */
window.$SD = $.SD;

})(jQuery);


$(document).ready(function(){
//document rady Start #########################################

// Top menu action Start
var onClickChangeEn 		= function(e){ e.preventDefault(); $("#langCode").val("en"); $("#chLanguage").submit(); };
var onClickChangeZh 		= function(e){ e.preventDefault(); $("#langCode").val("zh"); $("#chLanguage").submit(); };
var onClickChangeKo 		= function(e){ e.preventDefault(); $("#langCode").val("ko"); $("#chLanguage").submit(); };
var onClickSignOut 			= function(e){ e.preventDefault(); $("#signForm").attr("action", "/sa/mbr.logout.do"); $("#signForm").submit(); };
var onClickSignUp 			= function(e){ e.preventDefault(); $("#signForm").attr("action", "/signup"); $("#signForm").submit(); };
var onClickSignIn 			= function(e){ e.preventDefault(); $("#signForm").attr("action", "/sa/signIn.do"); $("#signForm").submit(); };
var onClickUserInfoUpdate 	= function(e){ e.preventDefault(); $("#signForm").attr("action", "/mypage/myforum/list.do"); $("#signForm").submit(); };
var onClickSignOff 			= function(e){ e.preventDefault(); $("#signForm").attr("action", "/sa/signOff.do"); $("#signForm").submit(); }; 
var onClickMyProfileUpdate 	= function(e){ e.preventDefault(); $("#signForm").attr("action", "/sa/update.profile.do"); $("#signForm").submit(); };
var onClickDeleteAccount 	= function(e){ e.preventDefault(); $("#signForm").attr("action", "/sa/signOff.do"); $("#signForm").submit(); };

$("#wrapper").on('click', 'a', function(e) {
	 switch($(this).attr('id')) {
	 case 'changeEn': onClickChangeEn(e);  break;
	 case 'changeZh': onClickChangeZh(e); break;
	 case 'changeKo': onClickChangeKo(e); break;
	 case 'signOut': onClickSignOut(e); break;
	 case 'signUp': onClickSignUp(e); break;
	 case 'signIn': onClickSignIn(e); break;
	 case 'userInfoUpdate': onClickUserInfoUpdate(e); break;
	 case 'signOff': onClickSignOff(e); break;
	 case 'myProfileUpdate' : onClickMyProfileUpdate(e); break;
	 case 'deleteAccount' : onClickDeleteAccount(e); break;
	 }
});
 
//Top menu action End


$("#sendFacebook, #sendTwitter").click(function(e) {
	e.preventDefault();
	var $this = $(this);
	
	if(typeof(copyUrl) != "undefined" && typeof(boardTitle) != "undefined") {
		var sns = $this.attr("id").substring(4).toLowerCase();
		switch(sns) {
		case "facebook" :
			var imgUrl = "http://img-developer.samsung.com/images/common/logo_200x200.gif";
			$("div.content img").each(function() {
				var that = $(this);
				if(that.width() > 200 && that.height() > 200) {
					imgUrl = that.attr("src");
					return false;
				}
			});
			
			var data = {
				app_id : $("#sd_appId").text(),
				link : copyUrl,
				picture : imgUrl,
				name : $("title").text(),
				caption : "developer.samsung.com",
				description : $("div.content p").eq(0).text(),
				redirectUri : "http://" + location.host + "/board/sns.do"
			};
			var url = "https://www.facebook.com/dialog/feed?" ;
			url += "app_id=" + data.app_id + "&" ;
			url += "link=" + data.link + "&" ;
			url += "picture=" + data.picture + "&" ;
			url += "name=" + encodeURIComponent(data.name) + "&" ;
			url += "caption=" + encodeURIComponent(data.caption) + "&" ;
			url += "description=" + encodeURIComponent(data.description) + "&" ;
			url += "redirect_uri=" + data.redirectUri ;
			sendSNS(sns, url, 850, 600);
			break;
		case "twitter" :
			sendSNS(sns, "http://twitter.com/home?status=" + encodeURIComponent(boardTitle) + " " + encodeURIComponent(copyUrl), 600, 400);
			break;
		}
	}
	
	function sendSNS(sns, url, iWidth, iHeight) {
		var popObj = { url : url
				     , width : iWidth
				     , height: iHeight
				     , target: sns
				     , scrollbars: "yes"
				     , resizeable: "yes"};
	
		$SD.popupCenter(popObj);
	}
})
 
//document rady End #########################################
 });

;(function(){
	window.deviceImageError = function(el) {
		var noImage = noImage || '/images/common/device_details_noimage.gif';
		if (el.src === noImage) 
			return;
		el.src = noImage;
	};
})();

function commonDownload(fileName, categoryId){
	if (fileName == "" || categoryId == ""){
		alert("필요한 인자값을 확인해주세요!!!!")
		return;
	}else{
		$SD.commonDownload(fileName, categoryId, function(data) {
		});
	}
}

function commonDownloadLog(fileFullPath, categoryId){
	if (fileFullPath == "" || categoryId == ""){
		alert("필요한 인자값을 확인해주세요!!")
		return;
	}else{
		$SD.commonDownloadLog(fileFullPath, categoryId, function(data) {
		});
	}
}

function commonDownloadLogTarget(fileFullPath, categoryId, target){
	if (fileFullPath == "" || categoryId == ""){
		alert("필요한 인자값을 확인해주세요!!")
		return;
	}else{
		$SD.commonDownloadLogTarget(fileFullPath, categoryId, target, function(data) {
		});
	}
}

function commonAllShareClickCount(fileFullPath, categoryId){
	if (fileFullPath == "" || categoryId == ""){
		alert("필요한 인자값을 확인해주세요!!")
		return;
	}else{
		$SD.commonAllShareClickCount(fileFullPath, categoryId, function(data) {
		});
	}
}

/*
function layer_view(id){

	var $layer = $('#'+id);
	var $down  = $('.license-layer').find('a#down');

	$layer.show();
	$layer.find('.close, #down').click(function(){
		$layer.hide();
	});

	function countChecked() {
		$(":checkbox").is(':checked') ? $down.show() : $down.hide()
	}

	$(":checkbox").click(countChecked);
}
*/
