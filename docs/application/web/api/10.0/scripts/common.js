$(document).ready(function(){
	$('#contents table').each(function(){
		if (!$(this).parent().hasClass('table')) {
			$(this).wrap('<div class="table"></div>');
		}
	});

	// Lnb Menu Initialize
	if($('div#contents').find('.lnb').length){
		if($("ul li.events_news").size() > 0) {
			$("ul.lnb").after("<p class=\"mt20\"><a href=\"/wearables\" target=\"_blank\"><img src=\"http://img-developer.samsung.com/images/common/img_sw_banner.gif\" alt=\"Samsung Wearables\"></a></p>");
		}
		initLnb();
		initScript(staticURL + "/js/fixednavbar.js", function(){});
	}

	//family site
	if($('div#footer').find('dl#familySlider').length){
		fn_rollToEx('familySlider', 'sliderBanner', 1, true);
	}

	// Svn Commit Test
	
	// Language Selection
	if($('div#header').find('.util').length){
		var $lang = $('div#header').find('.util');
		$lang.find('a.lang').toggle(function(){
				$(this).css('background-image', $(this).css('background-image').replace('.gif','_.gif')).next('ul.language').show();
			},function(){
				$(this).css('background-image', $(this).css('background-image').replace('_.gif','.gif')).next('ul.language').hide();
			});

		$lang.bind('mouseleave',function(){
			$(this).find('ul.language').hide();
			$lang.find('a.lang').css('background-image', $lang.find('a.lang').css('background-image').replace('_.gif','.gif'));
		});

		$lang.find('ul.language').children().last().on("keydown", function(e) {
			if(e.which == 9 && e.shiftKey) {
				return true;
			}
			
			if(e.which == 9) {
				e.preventDefault();
				$lang.find('ul.language').hide();
				$lang.find('a.lang').css('background-image', $lang.find('a.lang').css('background-image').replace('_.gif','.gif'));
				setTimeout(function() {
					$("#searchTop").focus();
				}, 1);
			}
		});
	}

	// Open the Sitemap
	var $open = $('div#header').find('.bt-open');
	$open.bind('click',function(){
		var $self = $(this);
		var $sitemap = $('div#wrapper').find('div#sitemap');
		//var source = $sitemap.is(':visible') ? $self.css('background-image').replace('_.gif','.gif') : $self.css('background-image').replace('.gif','_.gif');

		if($sitemap.is(':visible')){
			var source = $self.css('background-image').replace('_.gif','.gif');
			//if($('body#main').length) $('#header .util').css('border-bottom','3px solid #e4e4e4');

			$self.attr('title','open sitemap');
		}else{
			var source = $self.css('background-image').replace('.gif','_.gif');
			//if($('body#main').length) $('#header .util').css('border-bottom','3px solid #114196');

			$self.attr('title','close sitemap');
		}
		
		$self.css('background-image',source);
		$sitemap.slideToggle('fast');
		
		$sitemap.find('ul').filter(':last').children().filter(':last').focusout(function(){
			var source = $self.css('background-image').replace('_.gif','.gif');
			$self.css('background-image',source);
			$sitemap.slideToggle('fast');
		});

	});

	// Search Auto Complete
	var $search = $('div#header').find('fieldset.search');
	var $searchList = $search.find('#topAutocomplete>ul');

	if($search.length){
		$search.find('> input').each(function(){
			$(this).bind({
				keydown : function(e){
			
					if(e.type=='keydown'&& $(this).val().length!=0){
						$search.find('#topAutocomplete').show();
						var hei = $searchList.outerHeight();
						if(hei>400){
							$searchList.css({'height':'400px','overflow-y':'auto'});
						}
					}
					if(e.keyCode==9){
						$search.unbind('focusout.search');
					}
					if(e.keyCode==40){
						$search.find('#topAutocomplete>ul').children(':first').find('a').focus();
						//window.scrollTo(0,0);
					}
				},
				focusin : function(e){
					if($(this).val()==='Search'){
						$(this).val('');
					}
				},
				focusout : function(e){
					if($(this).val().length==0) $(this).val('Search');
				}
			});
		});

		//$('#topAutocomplete>ul').children().find('a').bind('focusin',function(e){
		//	if(e.keyCode==40){
		//		$(this).parent().next().css('border','1px solid red').find('a').focus();
		//	}
		//});

		$search.find('#topAutocomplete').bind('mouseleave',function(e){
			if($search.find('> input').val().length==0){
				$search.find('> input').val('Search');
			}
			$search.find('#topAutocomplete').hide();
		});

		$search.find('#topAutocomplete>ul').children().last().focusout(function(){
			$search.find('> input').val('Search');
			$search.find('#topAutocomplete').hide();
			
			//$search.bind('focusout.search', function(){
			//	$(this).find('> input').val('Search');
			//	$(this).find('#topAutocomplete').hide();
			//});
		});
	}
});

// 비차단 동적 스크립트 로딩
function initScript(url, callback){
	var script = document.createElement("script");
	script.type = "text/javascript";

	if(script.readyState){ // 인터넷 익스플로러
		script.onreadystatechange = function(){
			if(script.readyState=="loaded" || script.readyState=="complete"){
				script.onreadystatechange = null;
				callback();
			}
		};
	}else{	// 다른  브라우저
		script.onload = function(){
			callback();
		};
	}

	script.src = url;
	document.getElementsByTagName("head")[0].appendChild(script);
}


// lnb
function initLnb(){
	var sMenu = $('.lnb');
	var sItem = sMenu.find('>li');

	sItem.each(function(){
		if($(this).find('a').hasClass('more')){
			if($(this).find('ul').is(":visible")) {
				$('<button type="button" class="ico-arr">close submenu</button>').insertAfter($(this).find('a').eq(0));	
			} else {
				$('<button type="button" class="ico-arr">open submenu</button>').insertAfter($(this).find('a').eq(0));
			}
		}
	});
	
	var setIcoArrText = function(obj) {
		if(obj.next().is(":visible")) {
			obj.text("close submenu");
		} else {
			obj.text("open submenu");
		}
	}
	
	sItem.find('.ico-arr').on("click", function() {
		var $that = $(this);
		var liBox = $that.parent();   
		var ulBox = $that.next();
		
		sItem.not(liBox).not(".on").find("a.more").next().next().hide();
		sItem.not(liBox).removeClass("active").find("a").removeClass("bov");
		
		if(liBox.hasClass("on")) {
			if(ulBox.is(":visible")) {
				ulBox.hide();
				$that.addClass("ico-on");
			} else {
				ulBox.show();
				$that.removeClass("ico-on");
			}
			setIcoArrText($that);
			return true;
		}
		
		if(liBox.hasClass("active")) {
			liBox.removeClass("active").find("a").eq(0).removeClass("bov");
			ulBox.hide();
		} else {
			liBox.addClass("active").find("a").eq(0).addClass("bov");
			ulBox.show();
		}
		setIcoArrText($that);
	});

	sItem.hover(function(){
		if($(this).hasClass('on')||$(this).hasClass('active')) return false;
		$(this).find("a").eq(0).addClass("bov");
	},function(){
		if($(this).hasClass('on')||$(this).hasClass('active')) return false;
		 $(this).find("a").eq(0).removeClass("bov");

	});
}

//footer rolling banner
function fn_rollToEx(container,objectId,step,auto){

	// 롤링할 객체를 변수에 담아둔다.
	var el = $('#'+container).find('#'+objectId);
	var lastChild;
	var speed = 3000;
	var timer = 0;
	var autoplay = false;

	el.data('prev', $('#'+container).find('.prev'));	//이전버튼을 data()메서드를 사용하여 저장한다.
	el.data('next', $('#'+container).find('.next'));	//다음버튼을 data()메서드를 사용하여 저장한다.
	el.data('size', el.children().outerWidth());		//롤링객체의 자식요소의 넓이를 저장한다.
	el.data('len', el.children().length);				//롤링객체의 전체요소 개수
	el.data('animating',false);
	el.data('step', step);								//매개변수로 받은 step을 저장한다.
	el.data('autoStart', false);								//매개변수로 받은 step을 저장한다.

	el.css('width',el.data('size')*el.data('len'));		//롤링객체의 전체넓이 지정한다.

	if(arguments.length==4){
		el.data('autoStart', auto);
	}

	if(el.data('autoStart')){
		if(timer==0){
			timer = setInterval(moveNextSlide, speed);
			autoplay = true;
		}
	}

	el.bind({
		mouseenter:function(){
			if(!autoplay) return false;

			if(timer!=0 && el.data('autoStart')){
				clearInterval(timer);
				timer=0;
			}
		},
		mouseleave:function(){
			if(!autoplay) return false;

			if(timer==0 && el.data('autoStart')){
				timer = setInterval(moveNextSlide, speed);
			}
		}
	});


	//el에 첨부된 prev 데이타를 클릭이벤트에 바인드한다.
	el.data('prev').bind({
		click:function(e){
			e.preventDefault();
			movePrevSlide();
		},
		mouseenter:function(){

			$(this).find('img').addClass('btnOn');

			if(!autoplay) return false;

			if(timer!=0 && el.data('autoStart')){
				clearInterval(timer);
				timer=0;
			}
		},
		mouseleave:function(){

			$(this).find('img').removeClass('btnOn');

			if(!autoplay) return false;

			if(timer==0 && el.data('autoStart')){
				timer = setInterval(moveNextSlide, speed);
			}
		}
	});

	//el에 첨부된 next 데이타를 클릭이벤트에 바인드한다.
	el.data('next').bind({
		click:function(e){
			e.preventDefault();
			moveNextSlide();
		},
		mouseenter:function(){

			$(this).find('img').addClass('btnOn');

			if(!autoplay) return false;

			if(timer!=0 && el.data('autoStart')){
				clearInterval(timer);
				timer=0;
			}
		},
		mouseleave:function(){

			$(this).find('img').removeClass('btnOn');

			if(!autoplay) return false;

			if(timer==0 && el.data('autoStart')){
				timer = setInterval(moveNextSlide, speed);
			}
		}
	});

	function movePrevSlide(){
		if(!el.data('animating')){
			//전달된 step개수 만큼 롤링객체의 끝에서 요소를 선택하여 복사한후 변수에 저장한다.
			var lastItem = el.children().eq(-(el.data('step')+1)).nextAll().clone(true);
			lastItem.prependTo(el);		//복사된 요소를 롤링객체의 앞에 붙여놓는다.
			el.children().eq(-(el.data('step')+1)).nextAll().remove();	//step개수만큼 선택된 요소를 끝에서 제거한다
			el.css('left','-'+(el.data('size')*el.data('step'))+'px');	//롤링객체의 left위치값을 재설정한다.
		
			el.data('animating',true);	//애니메이션 중복을 막기 위해 첨부된 animating 데이타를 true로 설정한다.

			el.animate({'left': '0px'},'normal',function(){		//롤링객체를 left:0만큼 애니메이션 시킨다.
				el.data('animating',false);
			});
		}
		return false;
	}

    function moveNextSlide(){
		if(!el.data('animating')){
			el.data('animating',true);

			el.animate({'left':'-'+(el.data('size')*el.data('step'))+'px'},'normal',function(){	//롤링객체를 첨부된 size와 step을 곱한 만큼 애니메이션 시킨다.
				//전달된 step개수 만큼 롤링객체의 앞에서 요소를 선택하여 복사한후 변수에 저장한다.
				var firstChild = el.children().filter(':lt('+el.data('step')+')').clone(true);
				firstChild.appendTo(el);	//복사된 요소를 롤링객체의 끝에 붙여놓는다.
				el.children().filter(':lt('+el.data('step')+')').remove();	//step개수만큼 선택된 요소를 앞에서 제거한다
				el.css('left','0px');	////롤링객체의 left위치값을 재설정한다.

				el.data('animating',false);
			});
		}
		return false;
	}

}

function fn_slide(options){

	var opts = jQuery.extend({},options);

	var $bt = $('#'+opts.container).find('#'+opts.bt).children();					//롤링버튼에 대한 선택자
	var $obj = $('#'+opts.container).find('#'+opts.obj);								//objectId를 id로 갖는 롤링객체의 선택자
	var $prev = $('#'+opts.container).find('#'+opts.prev).hide();					//이전버튼에 대한 선택자
	var $next = $('#'+opts.container).find('#'+opts.next);							//다음버튼에 대한 선택자
	var size = $obj.children().outerWidth();				//롤링객체의 각 이미지 넓이값
	var len = $obj.children().length;						//롤링객체의 이미지 갯수
	var effect = false;										//슬라이드효과를 위한 boolean변수
	var auto = false;
	var current = 0;										//현재 보여지는 이미지의 인덱스값을 저장하기 위한 변수
	var time;


	$obj.css('width',size*len);								//롤링객체의 전체넓이 지정
	effect = opts.effect;
	auto = opts.auto;

	if(auto){
		time = setTimeout('slideShow()',3000);
	}

	slideShow = function(){

		if(current < len-1){
			current++;
		}else{
			current=0;
		}

		controllStatus();

		moveControl('next');

		time = setTimeout('slideShow()',3000);
	}

	controllStatus = function(){
		//이미지의 인덱스값에 따라 이전,다음 버튼 활성여부 지정
		if(current>0||current<len-1){				
			$prev.show();
			$next.show();
		}
		if(current==0){
			$prev.hide();
			$next.show();
		}
		if(current>=len-1){
			$prev.show();
			$next.hide();
		}
	}

	moveControl = function(msg){
		if(opts.bt!=null){
			msg=='next'? $bt.eq(current-1).find('img').attr('src', $bt.eq(current-1).find('img').attr('src').replace('_.png','.png'))
							:$bt.eq(current+1).find('img').attr('src', $bt.eq(current-1).find('img').attr('src').replace('_.png','.png'));	//이전에 활성화된 롤링버튼을 비활성화
			$bt.eq(current).find('img').attr('src', $bt.eq(current).find('img').attr('src').replace('.png','_.png'));		//현재 인덱스값을 가지는 롤링버튼을 활성화
		}

		if(effect!=true){				//action변수가 true가 아닐경우 슬라이드 효과없이 현재의 인덱스값을 갖는 이미지를 보여줌.
			$obj.children().hide();
			$obj.children().eq(current).show();
		}else{							//action변수가 true일 경우 현재의 인덱스값을 갖는 이미지로 슬라이드됨
			$obj.animate({'left':'-'+size*current},'slow');
		}
	}

	$obj.bind({
		mouseenter:function(){
			if(!auto) return false;
			clearTimeout(time);
		},
		mouseleave:function(){
			if(!auto) return false;
			time = setTimeout('slideShow()',3000);
		}
	});

	//롤링 버튼 클릭시
	$bt.bind({
		mouseenter:function(){
			if(!auto) return false;
			clearTimeout(time);
		},
		mouseleave:function(){
			if(!auto) return false;
			time = setTimeout('slideShow()',3000);
		},
		click:function(){
			var idx = $bt.index(this);					//클릭한 롤링버튼의 인덱스값 저장

			current = idx;								//롤링버튼의 인덱스값을 이미지의 인덱스값으로 지정

			controllStatus();

			if(effect!=true){				//action변수가 true가 아닐경우 슬라이드 효과없이 현재의 인덱스값을 갖는 이미지를 보여줌.
				$obj.children().hide();
				$obj.children().eq(current).show();
			}else{							//action변수가 true일 경우 현재의 인덱스값을 갖는 이미지로 슬라이드됨
				$obj.animate({'left':'-'+size*current},'slow');
			}

			// 모든 롤링 버튼을 비활성화
			$bt.each(function(){
				var source = $(this).find('img').attr('src').replace('_.png','.png');
				 $(this).find('img').attr('src',source);
			});

			// 선택한 롤링버튼을 활성화
			var source = $(this).find('img').attr('src').replace('.png','_.png');
			$(this).find('img').attr('src',source);

			return false;
		}
	});

	//이전 버튼 클릭시
	$prev.bind({
		mouseenter:function(){
			var source = $(this).find('img').attr('src').replace('.png','_.png');
			$(this).find('img').attr('src',source);
			if(!auto) return false;
			clearTimeout(time);
		},
		mouseleave:function(){
			var source = $(this).find('img').attr('src').replace('_.png','.png');
			$(this).find('img').attr('src',source);
			if(!auto) return false;
			time = setTimeout('slideShow()',3000);
		},
		click:function(){
			if(current==len-1) $next.show();	//이미지 인덱스값이 마지막이 아닐경우 비활성화된 다음버튼을 활성화	
			current--;							//이미지 인덱스값 1씩 감소

			moveControl('prev');

			if(current==0) $(this).hide();	//이미지 인덱스값이 0일 경우, 즉 현재 첫번째 이미지가 활성화될 경우 이전버튼을 비활성화

			return false;
		}
	});

	//다음 버튼 클릭시
	$next.bind({
		mouseenter:function(){
			var source = $(this).find('img').attr('src').replace('.png','_.png');
			$(this).find('img').attr('src',source);
			if(!auto) return false;
			clearTimeout(time);
		},
		mouseleave:function(){
			var source = $(this).find('img').attr('src').replace('_.png','.png');
			$(this).find('img').attr('src',source);
			if(!auto) return false;
			time = setTimeout('slideShow()',3000);
		},
		click:function(){
			current++;							//이미지 인덱스값 1씩 증가
			
			moveControl('next');

			if(current>=len-1) $(this).hide();	//이미지인덱스값이 마지막일 경우, 즉 현재 마지막 이미지가 활성화될 경우 다음버튼을 비활성화
			if(current>0) $prev.show();			//이미지인덱스값이 0이 아닌경우 이전버튼 활성화

			return false;
		}
	});

}

// main rolling banner
function slideMotion1(){
	var $banner = $('#rolling .motionview'),
		//$nav = $('#rolling ul.nav'),
		banner = {prev:null, next:null},
		size = $banner.children().length;
		index = 1,
		speed = 3000,
		timer = null,
		auto = true,
		width = parseInt(100/size),
		rest = parseInt(100%size);

	var $nav = $('<ul class="nav">').insertAfter($banner);

	$banner.children().each(function(index){
		index++;
		(index==1) ? $('<li style="width:'+width+'%;"><a href="'+ $(this).attr("href") +'" class="sel">'+index+'</a></li>').appendTo($nav) : $('<li style="width:'+width+'%;"><a href="'+ $(this).attr("href") +'">'+index+'</a></li>').appendTo($nav);
		if(index==size){
			$nav.children().eq(-1).find('a').css('background-image','none');
		}
	});

	if(rest>0){
		width+=rest;
		$nav.children().eq(-1).css('width',width+'%');
	}

	$nav.delegate("li",'click',function(){
		var idx = $nav.children().index(this);
		index = idx;
		banner.prev = $banner.find('a.active');
		banner.next = $banner.find('a').eq(index);

		clearInterval(timer);
		auto = false;
		
		$nav.trigger('change.banner',banner)
			.trigger('change.tab',index);

		return false;
	});

	$nav.bind('change.banner',function(event, banner){
		aniMotion();
	});

	$nav.bind('change.tab',function(event, index){
		$nav.children().find('a').removeClass('sel');
		$nav.children().eq(index).find('a').addClass('sel');
	});

	timer = setInterval(autoMotion, speed);

	function autoMotion(){
		if(index > size-1) index = 0;

		aniMotion();
	}

	function aniMotion(){
		if(auto){
			banner.prev = $banner.find('a.active');
			banner.next = $banner.find('a').eq(index);

			$nav.children().find('a').removeClass('sel');
			$nav.children().eq(index).find('a').addClass('sel');
		}
		banner.prev.addClass('last-active');
		banner.next.css({'opacity':0.0})
			.addClass('active')
			.animate({'opacity':1.0}, 1000, function(){
				banner.prev.removeClass('active last-active');

				if(auto){
					index++;
				}else{
					index++;
					timer = setInterval(autoMotion, speed*1.5);
					auto = true;
				}
			});
	}
}

// forum list show or hide function
function toggleFunc(){
	
	var defaulNum = [2];

	$('.forum-tit').each(function(){
		var self = $(this);

		var idx = $('.forum-tit').index(this);

		for(i=0;i<=defaulNum.length;i++){
			if(idx==defaulNum[i]){
				var source = self.find('a.toggle').css('background-image').replace('.gif','_.gif');
				self.find('a.toggle').css('background-image',source);

				self.find('a.toggle').text('Show');
				self.addClass('mb35').next().hide();
			}
		}

		self.find('a.toggle').click(function(){
			
			if(self.next().is(':visible')){
				var source = $(this).css('background-image').replace('.gif','_.gif');
				$(this).css('background-image',source);

				$(this).text('Show');
				self.addClass('mb35').next().hide();
			}else{
				var source = $(this).css('background-image').replace('_.gif','.gif');
				$(this).css('background-image',source);

				$(this).text('Hide');
				self.removeClass('mb35').next().show();
			}

			return false;

		});

	});
}

// 파일 업로드
function fileUpload( width ){
	//var $img = $('.attach input[type=image]');
	//var width = $img.attr('width');

	// 2012-08-08 추가 : 파일 input 너비영역 셋팅
	var w = width == null || width == undefined || isNaN( width ) ? "230px" : width + "px";

	var $file = $('.attach input.upload').css({
		"position": "absolute",
		"top": "0px",
		"right": "0px",
		"width": w,
		"cursor": "pointer",
		"opacity": "0.0",
		"height": "23px"
	});
	$file.off('change');
	$file.on('change',function(e){
		if(this.files != undefined && this.files.length == 0) { //chrome file 선택 취소시 파일 칸이 지워짐. 방지코드
			return;
		}
		var idx = $file.index(this);
		var localeCode = $("#localeCode").val() == undefined ? "en" : $("#localeCode").val();
		var fileErrMsg = {
				limit_ko : "최대 3개의 파일까지 업로드되며 200MB를 넘을수 없습니다"
			    ,limit_zh : "最多允许附加 3 个文件附件，并且其大小不能超过 200MB。"
			    ,limit_en : "Up to 3 file attachments are allowed and its size cannot exceed 200MB"
			    ,ext_ko : "지원하지 않는 확장자 입니다."
			    ,ext_zh : "不允许上传具有该扩展名的文件。"
			    ,ext_en : "File extention not allowed for upload."
		};
		var initFileInput = function(obj) {
			$(obj).parent().find('input.file').val("");
			if($.browser.msie && $.browser.msie && $.browser.version < 10.0  ) $(obj).replaceWith( $(obj).clone(true) );
			else $(obj).val("");
		};
		
		var filename = $(this).val();
		
		//CHK File ext
		var imgExts = [ "txt", "xls", "xlsx", "doc", "docx"
			              , "ppt", "pptx", "pdf", "bmp", "gif", "jpeg"
			              , "jpg", "png", "zip"];
		var fileExt  = filename.substring(filename.lastIndexOf(".") + 1).toLowerCase();
		var findFlag = false;
		for(var i = 0; i < imgExts.length; i++) {
			if(imgExts[i] == fileExt) {
				findFlag = true;
				break;
			}
		}
	
		if(findFlag == false) {
			alert( fileErrMsg["ext_" + localeCode] );
			initFileInput(this);
//			setTab(localeCode); //thread_write에도 있는데 실제로 본체가 없음.
			return;
		}
		
		//CHK File Size
		if(
				($.browser.msie && $.browser.version >= 10.0 ) //msie
				|| $.browser.mozilla //FF
				|| $.browser.safari //Chrome
		)
		{
			var filesize = parseInt(this.files[0].size/1024/1024); //MB;
			if( filesize > 200 ) {
				alert( fileErrMsg["limit_" + localeCode] );
				initFileInput(this);
				return;
			}
		}
		
		$(this).parent().find('input.file').attr("disablesd","disabled").val(filename);
	});
};


// Show or Hide Toggle
function showToEx(args){

	if(!arguments.length) return false;
	
	var bt = $('#'+args.bt);
	var obj = $('#'+args.obj);

	var source = bt.css('background-image');
	
	if(obj.is(':visible')){
		obj.hide();
	}

	bt.toggle(function(){
		var src = source.replace('.gif','_.gif');
		bt.css('background-image', src);
		obj.show();
		
		return false;
	},function(){
		var src = source.replace('_.gif','.gif');
		bt.css('background-image', src);
		obj.hide();

		return false;
	});

}


// FAQ 20131016
function faqToEx(){

 var $question = $('#contents').find('.question');
 var $answer = $('#contents').find('.answer');

 // All Answer Rows Hide
 $answer.hide().find('.conts').hide();

 $question.each(function(){
  var $self = $(this);
  $self.append("<div style='display: none'>" + $self.find("a").html() + "</div>");
  
  $self.find('a').bind('click',function(){
   $("#selArea ul").hide();
   /*
   if($(this).parents('tr').next().find('.answer').is(':visible')) return false;

   $answer.hide().find('.conts').hide();
   $(this).parents('tr').next().find('.answer').show().find('.conts').slideDown('normal');
   */

   /* 20120822 hjh modify*/
   /* if ( this open )?  close : all close, e.target open */
   var cutTtl  = $(this).parent().children("div").html();
   var ttl     = $(this).parent().parent().children("td.real_question").html();
   
   if($(this).parents('tr').next().find('.answer').is(':visible')){
    $(this).html(cutTtl);
    $(this).parents('tr').next().find('.answer').find('.conts').slideUp('fast',function(){
     $answer.hide();
    });
   }else{
    titleInit();
    $(this).html(ttl);
    $answer.hide().find('.conts').hide();
    //$answer.slideUp('normal').find('.conts').hide();
    $(this).parents('tr').next().find('.answer').show().find('.conts').slideDown('slow'); 
   }   

   return false;
  });
 });

 $answer.each(function(){
  var $self = $(this);

  $(this).find('a.bt-close-faq').bind('click',function(){
   var question_td = $(this).parent().parent().parent().prev().children("td.question");
   var cutTtl      = question_td.children("div").html();
   question_td.children("a").html(cutTtl);
   
   $self.find('.conts').slideUp('fast',function(){
    $self.hide();
   });

   return false;
  });
 });
 
 var titleInit = function() {
  $question.each(function(i) {
   $(this).find("a").html($(this).find("div").html());
  });
 }
}



/**
 *  쓰기페이지 Tab 영역 컨트롤
 *  @param	selector	텝을 선택했을 때 교체할 레이어 선택자 ex) '.bbs-write:not(#opt)'
 */
function setSwitchTab( selector ) {
	var tabs = $('.tab-list').find("li");
	var elements = $( selector );

	$( elements ).each( function( i ) {
		if( i != 0 )
		{
			$(this).hide();
		}
	})

	// Control Tabs
	$( tabs ).each( function( i ) {
		$( this ).click( function(){
			resetClass();

			$( this ).find( 'a' ).addClass( "sel" );
			$( elements[i] ).show();

			return false;
		});
	});

	// Class 리셋
	function resetClass()
	{
		$( tabs ).each( function( i ) {
			$( this ).find( 'a' ).removeClass( 'sel' );
		});

		$( elements ).each( function( i ) {
			$( this ).hide();
		});
	}
}

var SET_ATTACH_LIMIT;
var SET_ATTACH_WIDTH;
var SET_ATTACH_BTNNAME;

var firstAddAction = function(obj, limit, w, btnName) {
 var bn            = btnName || 'File';
 var fileAttachStr = "<li class='clfix no-first'>";
 fileAttachStr += '<div class="attach">';
 fileAttachStr += '<input readonly="readonly" disabled="disabled" type="text" class="ipt-txt file" />';
 fileAttachStr += '<span class="fbtn" style="margin-left: 4px;">' + bn + '</span>';
 fileAttachStr += '<input type="file" name="file" class="upload" title="File upload" />';
 fileAttachStr += '</div>';
 fileAttachStr += '<a href="#none" class="remove-btn fl" style="margin-left: 3px;">remove file</a>';
 fileAttachStr += '</li>';
 obj.on("keydown", function(e) {
  if(e.which == 9 && e.shiftKey) {
   e.preventDefault();
   setTimeout(function() {
    $("a.remove-btn").eq(0).focus();
   }, 1);
  }
 });
 
 obj.click( function()
 {
  var ul = $( this ).parentsUntil( $("td"), ".file-att-form" );
  
  if( $( ul ).find( "li" ).length >= limit )
  {
   alert( "Only " + limit + " files are allowed" );
   return;
  }
  //$( fileAttachStr ).find( ".ipt-txt" ).css("width", w + "px" );
  $( ul ).append( fileAttachStr );
  var removeBtns = $( ul ).find( ".remove-btn" ).last();
  $( removeBtns ).bind( "click", onBtnFileDetachClick );
  
  
  removeBtns.on("keydown", function(e) {
   var that = $(this);
   if(e.which == 9 && e.shiftKey) {
    e.preventDefault();
    setTimeout(function() {
     that.prev().find("input[type=file]").focus();
    }, 1);
   }
  });
  
  var addInputFile = $("ul.file-att-form input[type=file]").last(); 
  
  addInputFile.on("keydown", function(e) {
   var that = $(this);
   if(e.which == 9 && e.shiftKey) {
    return true;
   }
   
   if(e.which === 9) {
    e.preventDefault();
    setTimeout(function() {
     that.parent().parent().find("a.remove-btn").eq(0).focus();
    }, 1);
   }
  }).on("focusin", function(e) {
   $(this).parent().css("outline", "1px dotted #2d2d2d");
  }).on("focusout", function(e) {
   $(this).parent().css("outline", "");
  });

  fileUpload( w + 50 );
  updateFileField();
  return false;
 });
 
 function onBtnFileDetachClick()
 {
  var that = $(this);
  $( this ).unbind( "click", onBtnFileDetachClick );
   var a = that.parent().prev().children("a").eq(0);
   setTimeout(function() {
   that.parents(".no-first").remove();
  }, 1);
  
  setTimeout(function() {
   a.focus();
  }, 300);
  return false;
 }
 
 function updateFileField()
 {
  var ul = $( ".file-att-form" );
  $( ul ).find( ".ipt-txt" ).css( "width", w + "px" );
 }
}

var firstRemoveAction = function(id) {
 var obj = $("#" + id);
 var compFile    = $("input[type=file]");
 var compFileCnt = compFile.size();
 var ulObj       = compFile.eq(0).parent().parent().parent();
 if(compFileCnt <= 1) {
  var firstCompFile = compFile.eq(0);
  firstCompFile.prev().prev().val("");
  if ($.browser.msie) {
		$(obj).parent().find('input.file').val("");
		firstCompFile.replaceWith( firstCompFile.clone(true) );
	} else {
		firstCompFile.val("");
		firstCompFile.prev().prev().val("");
  }
 } else {
  obj.parent().remove();
  ulObj.find("a.remove-btn").eq(0).after("<a href=\"JAVA-SCRIPT:;\" class=\"add-btn fl\" style=\"margin-left: 3px;\">add file</a>");
  
  //add-btn event..
  firstAddAction($("a.add-btn"), SET_ATTACH_LIMIT, SET_ATTACH_WIDTH, SET_ATTACH_BTNNAME);
 }
 
 ulObj
 .find("li")
 .eq(0)
 .removeClass("no-first")
 .find("a.remove-btn")
 .attr("id", id)
 .unbind("click");
 
 setTimeout(function() {
  $("#" + id).focus();
 }, 100);
 
 $("#" + id).on("keydown", function(e) {
  if(e.which == 9 && e.shiftKey) {
   e.preventDefault();
   var that = $(this);
   setTimeout(function() {
    that.prev().focus();
   }, 1);
  }
 });
 
 $("#" + id).on("click", function(e) {
  firstRemoveAction($(this).attr("id"));
 });
}

/** 
 * File 첨부컨트롤
 * @param limit 최대 파일 첨부 갯수
 * @param width 파일 업로드 필드의 너비 <- 2012-08-08 추가
 */
function setAttachFile( limit, width, btnName, removeBtnId )
{
 var w = width == null || width == undefined  || isNaN( width ) ? 180 : width;
 var btnFileAttach = $( 'ul.file-att-form' ).find( 'a.add-btn' );
 var inputFile     = $( 'ul.file-att-form input[type=file]' );
 
 SET_ATTACH_LIMIT = limit;
 SET_ATTACH_WIDTH = w;
 SET_ATTACH_BTNNAME = btnName;
 
 inputFile.on("keydown", function(e) {
  var that = $(this);
  
  if(e.which == 9 && e.shiftKey) {
   return true;
  }
  
  if(e.which === 9) {
   e.preventDefault();
   setTimeout(function() {
    that.parent().parent().find("#" + removeBtnId).eq(0).focus();
   }, 1);
  }
 });
 
 inputFile.on("focusin", function(e) {
  $(this).parent().css("outline", "1px dotted #2d2d2d");
 }).on("focusout", function(e) {
  $(this).parent().css("outline", "");
 });
 
 firstAddAction(btnFileAttach, limit, w, btnName);
 
 /*
 btnFileAttach.on("keydown", function(e) {
  if(e.which == 9 && e.shiftKey) {
   e.preventDefault();
   setTimeout(function() {
    inputFile.focus();
   }, 1);
  }
 });
 
 btnFileAttach.click( function()
 {
  var ul = $( this ).parentsUntil( $("td"), ".file-att-form" );
  
  if( $( ul ).find( "li" ).length >= limit )
  {
   alert( "Only " + limit + " files are allowed" );
   return;
  }
  //$( fileAttachStr ).find( ".ipt-txt" ).css("width", w + "px" );
  $( ul ).append( fileAttachStr );
  var removeBtns = $( ul ).find( ".remove-btn" ).last();
  $( removeBtns ).bind( "click", onBtnFileDetachClick );
  
  
  removeBtns.on("keydown", function(e) {
   var that = $(this);
   if(e.which == 9 && e.shiftKey) {
    e.preventDefault();
    setTimeout(function() {
     that.prev().find("input[type=file]").focus();
    }, 1);
   }
  });
  
  var addInputFile = $("ul.file-att-form input[type=file]").last(); 
  
  addInputFile.on("keydown", function(e) {
   var that = $(this);
   if(e.which == 9 && e.shiftKey) {
    return true;
   }
   
   if(e.which === 9) {
    e.preventDefault();
    setTimeout(function() {
     that.parent().parent().find("a.remove-btn").eq(0).focus();
    }, 1);
   }
  }).on("focusin", function(e) {
   $(this).parent().css("outline", "1px dotted #2d2d2d");
  }).on("focusout", function(e) {
   $(this).parent().css("outline", "");
  });

  fileUpload( w + 50 );
  updateFileField();
  return false;
 });
 

 // File 제거 버튼
 function onBtnFileDetachClick()
 {
  var that = $(this);
  $( this ).unbind( "click", onBtnFileDetachClick );
   var a = that.parent().prev().children("a").eq(0);
   setTimeout(function() {
   that.parents(".no-first").remove();
  }, 1);
  
  setTimeout(function() {
   a.focus();
  }, 300);
  return false;
 }
 */
 /**
  *  2012-08-08 전종호 추가
  *  파일 Input Text 영역 너비를 잡아주는 메서드
  */
 function updateFileField()
 {
  var ul = $( ".file-att-form" );
  $( ul ).find( ".ipt-txt" ).css( "width", w + "px" );
 }

 updateFileField();
 fileUpload( w + 50 );
 
 $("#" + removeBtnId).on("click", function(e) {
  firstRemoveAction($(this).attr("id"));
 });
}



/** 
 * [PAGE] device speces list page
 * date : 20120808
 * id : hjh
 */
function initDevicespecsList (){
	var isCompareView=false;
	$("#devicespecs-list > li").each( 
		function(i){ 
			$(".info", this).bind("click", devicespecsListInfoToggle);
			$(".xx", this).bind("click", devicespecsListInfoToggle);
			
			//detail info layer toggle function
			function devicespecsListInfoToggle (){
				$("#devicespecs-list li:nth-child("+(i+1)+") .info-detail").toggle();
				return false;
			}
	});


	/* DEVICE COMPARE 열리는 부분
	- defualt : close. 
	- 최초 한번만 열림 
	- 현재는 compare 버튼에 공통으로 함수 바인딩
	*/
	function devicespecsCompareOnOff (){
		if ( isCompareView ) return;
		var ww = ( isCompareView ) ? "30px":"207px";
		$("#devicespecs-compare").animate({
		    height: ww }, 300, "linear", function(){ });

		isCompareView = ( isCompareView ) ? false:true;
		return false;
	}

	//compare 버튼 공통으로 클릭 이벤트 걸림 
	$(".compare").bind("click", function (){ devicespecsCompareOnOff() });
}

/** 
 * [PAGE] device speces view page
 * date : 20120808
 * id : hjh
 */
 function initDevicespecsView (){
	var isImgView = false;
	var isView = 0;
	
	//thumbnail overevent bind
	$("#img-viewer-thumbnail > li").each( function(i){ $(this).bind("mouseover focusin",function(){focusDeviceDetail(i+1);}); } );
	focusDeviceDetail (1);
	
	$("#img-viewer-thumbnail li").last().on("keydown keyup", function(e) {
		if(e.which == 9 && e.shiftKey) {
			return true;
		}
		
		if(e.type === "keydown" && e.which == 9) {
			setTimeout(function() {
				$("#img-viewer-handle a").eq(0).focus();	
			}, 1);
		}
	});
	
	//thumbnail viewarea controll handler bind
	$("#img-viewer-handle").click(function () {
		var ww;
		var src = $("#img-viewer-handle img").attr("src");
		if ( isImgView ){
			ww = "300px";
			src = src.replace(".gif", "_.gif");
			$("#img-viewer-thumbnail").hide();
			$("#device-info").show();
		}else{
			ww = "730px";
			src = src.replace("_.gif", ".gif");
			$("#img-viewer-thumbnail").show();
			$("#device-info").hide();
			focusDeviceDetail(1);
		}
		
		$("#img-viewer-handle img").attr("src", src);
    	$("#img-viewer").animate({
		    width: ww
			}, 300, "linear", function(){
			if($.browser.msie)
				$("#img-inner").css("width", ww);
		});
		
    	isImgView = ( isImgView ) ? false:true;
    });

	//thumbnail overevent function (update date 2012.09.05 kangki)
	function focusDeviceDetail ( id ) {
		if ( isView == id ) return;

		$("#img-viewer-thumbnail li:nth-child("+isView+")").removeClass ("on");
		var imgSrc = $("#img-viewer-thumbnail li:nth-child("+id+")").addClass ("on").find('img').attr('src');

		$( "#img-viewer-bic > img").attr("src", imgSrc);
		isView = (id);		
	}

	/*toggle devicespecs List*/
	if($('div#contents').find('.devicespec-tit').length){
		
		$('.devicespec-tit').each(function(){
			var self = $(this);
			$('a', self).bind ("click", fnToggle);

			function fnToggle(){

				if ( $(this).parent().parent().next().is(':visible') ){
					$(this).css('background-image', $(this).css('background-image').replace('.gif','_.gif'));

					self.find('em').text('Show');
					self.next().hide();

					return false;
				}else{
					$(this).css('background-image', $(this).css('background-image').replace('_.gif','.gif'));
					self.find('em').text('Hide');
					self.next().show();

					return false;
				}
			}
							
		});
	}

	/*all Show Hide devicespecs List*/
	if($('div#contents').find('.devicespecs-util').length){
		var self = $('div#contents').find('.devicespecs-util');

		$('.showA', self).bind ("click", function (){
			$('.devicespec-tit').each(function(){

				var me = $(this);
				if ( !me.next().is(':visible') ){
					me.find("a").css('background-image', me.find("a").css('background-image').replace('_.gif','.gif'));
					me.find('em').text('Hide');
					me.next().show();
				}
			});
			return false;
		})
		$('.hideA', self).bind ("click", function (){
			
			$('.devicespec-tit').each(function(){

				var me = $(this);
				if ( me.next().is(':visible') ){
					me.find("a").css('background-image', me.find("a").css('background-image').replace('.gif','_.gif'));
					me.find('em').text('Show');
					me.next().hide();
				}
								
			});
			return false;
		})
	}	
}

/** 
 * [PAGE] Search Result
 * date : 20120810
 * author : 전종호
function searchInit()
{
	var focusTarget = "input";

	$("#searchInput").bind("keydown", checkSearchText);
	$("#searchInput").focusout(function() {
		if( focusTarget == "dropdown" )
		{
			return false;
		}
		else
		{
			//toggleClass( false );
		}
	});
	
	$( "#searchInput" ).focusin( function()	{
		focusTarget = "input";
	});

	$("#btnDropdown").mousedown( function(){
		focusTarget = "dropdown";
	});

	$(".autocomplete ul li").focusin( function() {
		//
	});

	$(".autocomplete ul li:last-child").focusout( function() {
		toggleClass( false );
	})

	$(".autocomplete").mouseleave(function(){
		toggleClass( false );
	});
	
	$("#btnDropdown").click( function(){
		//alert("btn click");
		if( $("#searchInput").val().length == 0 ){ 
			return false;
		}
		else{
			if( $("#btnDropdown").hasClass("dropdown") ){
				toggleClass( true );
			}
			else{
				toggleClass( false );
			}
		}

		return false;
	});

	function checkSearchText(){
		setTimeout(function(){
			var txt = $("#searchInput").val();

			if( txt.length > 0 ){
				toggleClass( true );
			}
			else{
				toggleClass( false );	
			}
		}, 1);
	}

	function toggleClass( bo ){
		if( bo ){
			$(".autocomplete").css("visibility", "visible");

			$("#btnDropdown").removeClass("dropdown");
			$("#btnDropdown").addClass("dropdownoff");

			var hei = $(".autocomplete").find('>ul').outerHeight();
			if(hei>400){
				$(".autocomplete").css({'height':'400px','overflow-y':'auto'});
			}
		}
		else{
			$(".autocomplete").css("visibility", "hidden");
			
			$("#btnDropdown").removeClass("dropdownoff");
			$("#btnDropdown").addClass("dropdown");
		}
	}
}
 */

function setTopScroll(selector) {
	if ( !selector ) return false;
	var btn = $( selector );
	var w = $( window );
	btn.css( "position", "absolute" );


	btn.click( function(){ w.scrollTop( 0 ) } );

	var wheight = w.innerHeight();
	
	$(window).resize( function() {
		wheight = w.innerHeight();
		redraw();
	});

	$(window).scroll( function() {
		redraw();
	})

	/**
	 *	Top 버튼의 재정렬 메서드
	 */
	function redraw()
	{
		var t = w.scrollTop() + wheight - 289;

		if( t < wheight / 2 && w.scrollTop() == 0 )	{
			t = wheight / 2;
		}
		
		btn.clearQueue();

		btn.animate({
	    top: t
	  	}, 500, function() {
	    // Animation complete.
	  	});
		//btn.css( "top", t );
		//console.log( "target : " + t );
	}

	redraw();
	/*
	obj.initTop = position;
	obj.topLimit = topLimit;
	obj.bottomLimit = Math.max( document.documentElement.scrollHeight, document.body.scrollHeight ) - btmLimit - obj.offsetHeight;

	obj.style.position = "absolute";
	obj.top = obj.initTop;
	// obj.left = obj.initLeft;

	if ( typeof( window.pageYOffset ) === "number" ) {	//WebKit
		obj.getTop = function() {
			return window.pageYOffset;
		}
	} else if ( typeof( document.documentElement.scrollTop ) === "number" ) {
		obj.getTop = function() {
			return Math.max( document.documentElement.scrollTop, document.body.scrollTop );
		}
	} else {
		obj.getTop = function() {
			return 0;
		}
	}

	if ( self.innerHeight ) {	//WebKit
		obj.getHeight = function() {
			return self.innerHeight;
		}
	} else if( document.documentElement.clientHeight ) {
		obj.getHeight = function() {
			return document.documentElement.clientHeight;
		}
	} else {
		obj.getHeight = function() {
			return 500;
		}
	}

	obj.move = setInterval( function() {
		if ( obj.initTop > 0 ) {
			pos = obj.getTop() + obj.initTop;
		} else {
			pos = obj.getTop() + obj.getHeight() + obj.initTop;
		}

		if ( pos > obj.bottomLimit ) pos = obj.bottomLimit;
		if ( pos < obj.topLimit ) pos = obj.topLimit;

		interval = obj.top - pos;
		obj.top = obj.top - interval / 3;
		obj.style.top = obj.top + "px";
	}, 30 )
	*/
}


//popup
function pop(url,name,w,h){window.open(url,name,'width='+w+',height='+h+',scrollbars=no')} //Popup(스크롤바없음)
function pops(url,name,w,h){ window.open(url,name,'width='+w+',height='+h+',scrollbars=yes') } //Popup(스크롤바있음)

//popup 중앙에 띄우기
function pop_center(){ 
	var x,y; 
	if (window.innerHeight) { // IE 외 모든 브라우저 
		x = (screen.availWidth - self.innerWidth) / 2; 
		y = (screen.availHeight - self.innerHeight) / 2; 
	}else if (document.documentElement && document.documentElement.clientHeight) { // Explorer 6 Strict 모드 
		x = (screen.availWidth - document.documentElement.clientWidth) / 2; 
		y = (screen.availHeight - document.documentElement.clientHeight) / 2; 
	}else if (document.body) { // 다른 IE 브라우저( IE &lt; 6) 
		x = (screen.availWidth - document.body.clientWidth) / 2; 
		y = (screen.availHeight - document.body.clientHeight) / 2; 
	} 
	window.moveTo(x,y); 
}

// Layer Popup Open
function layer_open(el){
	var temp = $('#' + el);

	if(!temp.hasClass('sty2')){
		$('.layer').fadeIn();
	}

	if (temp.outerHeight() < $(document).height() ) temp.css('margin-top', '-'+temp.outerHeight()/2+'px');
	else temp.css('top', '0px');
	if (temp.outerWidth() < $(document).width() ) temp.css('margin-left', '-'+temp.outerWidth()/2+'px');
	else temp.css('left', '0px');

	if(temp.hasClass('sty2')){
		temp.fadeIn();

		temp.find('a.cbtn').click(function(e){
			temp.fadeOut();
		});
		temp.find('a.gbtn').click(function(e){
			temp.fadeOut();
		});

		return false;
	}
	// 닫는 버튼 gbtn-c 추가 20130627
	$('.layer .bg, .pop-header .close, .gbtn-c').click(function(){
		$('.layer').fadeOut();
		return false;
	});
}

// background dim - 2013-05-31
function layer_open2(el){
	var temp = $('#' + el);
	$('input').attr('disabled', 'disabled');
	$('.layerPop').fadeIn();
	

	if (temp.outerHeight() < $(document).height() ) temp.css('margin-top', '-'+temp.outerHeight()/2+'px');
	else temp.css('top', '0px');
	if (temp.outerWidth() < $(document).width() ) temp.css('margin-left', '-'+temp.outerWidth()/2+'px');
	else temp.css('left', '0px');

	$('.layerPop .bg, .pop-header .close, .gbtn, .cbtn').click(function(){
		$('.layerPop').fadeOut();
		$('input').removeAttr('disabled');
		return false;
	});
}


function pop_account(url){
	window.open(url,'account','width=619,height=591,scrollbars=yes')
}

function pop_loadDoc(url){
	window.open(url,'online','width=850,height=600,scrollbars=yes')
}

/** 
 *  [PAGE] Tags
 *  date : 20120820
 *  author : 전종호
 */
function initTags()
{
	// Tag리스트의 각 엘리먼트 뒤에 "," 리터럴 추가.
	// 마지막 아이템은 제외
	var eleArr = $(".tag-list").find("li");

	$( eleArr ).each( function( i ) {
		if( i < eleArr.length - 1 )
		{
			var target = $(this).find("a")[0];
			var content = $( target ).html();

			$( target ).html( content + "," );
		}
	})
}

$(document).ready(function(){
	$(".tip_info").css("cursor","pointer");
	$(".tip_info > img").mouseover(function(){
		$(".tip_cont").css("display","block");
	});
	$(".tip_info > img").mouseout(function(){
		$(".tip_cont").css("display","none");
	});
});

// new layer popup script by ygh 2013.11.14

var isPopup = false ;

function popupLayerView(id){

	var $L = $("#" + id) ;
	var $D  = $("#" + id + "down") ;

	$T = $("#" + id) ;

	$L.show();
	isPopup = true ;

	$('html, body').animate({ scrollTop: $L.offset().top }, 500);

	$("#" + id + "agree").focus() ;

	jQuery(":focusable").focusin(function(e){
		if (isPopup) {
			e.stopPropagation() ;
			if ($L.find(jQuery(this)).length > 0) {
			} else {
				jQuery(this).blur() ;
				jQuery("#" + id + " :focusable:first").focus() ;
			}
		}
	}) ;

	$L.find('.close').click(function(){
		resetPopup(id) ;
	});

	$("#" + id + "agree").click(function() { $(this).is(':checked') ? $D.show() : $D.hide() ; });
}

function resetPopup(T) {
	$("#" + T + "down").hide();
	$("#" + T + "agree").attr("checked", false) ;
	isPopup = false ;
	$("#" + T).hide() ;
	$("#" + T + "Btn").focus() ;
}

function getDownload(T, F, I) {
	if ($("#" + T + "agree").is(':checked')) {
		commonDownloadLog(F, I) ;
		resetPopup(T) ;
	}
}

function focusable( element, isTabIndexNotNaN ) {
	var map, mapName, img, nodeName = element.nodeName.toLowerCase() ;
	if ( "area" === nodeName ) {
		map = element.parentNode;
		mapName = map.name;
		if ( !element.href || !mapName || map.nodeName.toLowerCase() !== "map" ) { return false ; }
		img = $( "img[usemap=#" + mapName + "]" )[0];
		return !!img && visible( img );
	}
	return ( /input|select|textarea|button|object/.test( nodeName ) ? !element.disabled : "a" === nodeName ? element.href || isTabIndexNotNaN : isTabIndexNotNaN) && // the element and all of its ancestors must be visible
			visible( element ) ;
}

function visible( element ) {
	return $.expr.filters.visible( element ) && !$( element ).parents().addBack().filter(function() {
		return $.css( this, "visibility" ) === "hidden";
	}).length;
}
if ( !$.fn.addBack ) { $.fn.addBack = function( selector ) { return this.add( selector == null ? this.prevObject : this.prevObject.filter( selector ) ); }; }

$.extend( $.expr[ ":" ], {
	data: $.expr.createPseudo ? $.expr.createPseudo(function( dataName ) { return function( elem ) { return !!$.data( elem, dataName ); }; }) : function( elem, i, match ) { return !!$.data( elem, match[ 3 ] ); },
	focusable: function( element ) { return focusable( element, !isNaN( $.attr( element, "tabindex" ) ) ); },
	tabbable: function( element ) { var tabIndex = $.attr( element, "tabindex" ), isTabIndexNaN = isNaN( tabIndex ); return ( isTabIndexNaN || tabIndex >= 0 ) && focusable( element, !isTabIndexNaN ); }
});
// new layer popup script by ygh 2013.11.14

// 2013-11-15 타이젠 썸네일 추가
$(document).ready(function() {
	$('.view_device1').hide();
	
	$('#thumb_view_btn').hover(function() {
		$('.view_device1').show();
	},function() {
		$('.view_device1').hide();
	});
		
});

// 2014-04-22 타이젠 썸네일 추가
$(document).ready(function() {
	$('.view_device2').hide();
	
	$('#thumb_view_btn2').hover(function() {
		$('.view_device2').show();
	},function() {
		$('.view_device2').hide();
	});
		
});


function beforePopupLayerView(popId, popId2, popContinue){
	var $L = $("#" + popId) ;
	$L.show(100);
	$('html, body').animate({ scrollTop: $L.offset().top }, 500);
	$L.find('.close').click(function(){
		$L.hide();
	});
	$L.find("." + popContinue).click(function() { $L.hide(); popupLayerView(popId2); });
}
