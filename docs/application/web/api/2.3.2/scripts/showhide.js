/*all Show Hide devicespecs List*/
if($('div#contents').find('.devicespecs-util').length){
var self = $('div#contents').find('.devicespecs-util');

$('.showA', self).bind ("click", function (){
$(this).parents('.devicespecs-util').next().find('.devicespec-tit').each(function(){
var me = $(this);
var idx = $('.devicespecifications .devicespec-tit').index(this);

if ( !me.next().is(':visible') ){
	me.find("a").css('background-image', me.find("a").css('background-image').replace('_.gif','.gif'));
	me.find('em').text('Hide');
	me.next().show();
}
});
return false;
})
$('.hideA', self).bind ("click", function (){
$(this).parents('.devicespecs-util').next().find('.devicespec-tit').each(function(){

	var me = $(this);
	var idx = $('.devicespecifications .devicespec-tit').index(this);

	if ( me.next().is(':visible') ){
		me.find("a").css('background-image', me.find("a").css('background-image').replace('.gif','_.gif'));
		me.find('em').text('Show');
		me.next().hide();
	}
					
});
return false;
})
}	

/*toggle devicespecs List*/
if($('div#contents').find('.devicespec-tit').length){

$('.devicespec-tit').each(function(){
var self = $(this);
$('a', self).bind ("click", function(){
	var idx = $('.devicespec-tit a').index(this);

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

});

});
}

$('ul.devicespecifications li div.devicespec-con').hide();


$('.devicespec-tit').each(function(){
var self = $(this);
var arrow =  $('a', self);

if(self.next().is(':visible')){
arrow.css('background-image', arrow.css('background-image').replace('_.gif','.gif'));
self.find('em').text('Hide');
}else{
arrow.css('background-image', arrow.css('background-image').replace('.gif','_.gif'));
self.find('em').text('Show');
}

});

$(document).ready(function(){
	var openheading = function(target) {
		var origin = $(target);
		target = origin.closest('.devicespec-con');
		if (!(target.length > 0)) {
			target = origin.closest('.devicespec-tit');
		}
		if (target.length > 0) {
			if (!$('.devicespec-con', target.parent()).is(":visible")) {
				$("div.devicespec-tit a.bt-arr", target.parent()).click();
			}
		}

		$(window.location.hash)[0].scrollIntoView();
	};

	$(".opensection").click(function(){
		var target = $($(this).attr("href"));//.closest('.devicespec-con');
		openheading(target);
	});

	if (window.location.hash) {
		var target = $(window.location.hash);
		openheading(target);
		//$(target).focus(); //uncomment if fail to work
	}

	var isScrolledIntoView = function(elem)
	{
		var docViewTop = $('#contents').scrollTop();
		var docViewBottom = docViewTop + $('#contents').height();

		var elemTop = $(elem).offset().top;
		var elemBottom = elemTop + $(elem).height();

		return ((elemBottom >= docViewTop) && (elemTop <= docViewBottom)
		  && (elemBottom <= docViewBottom) &&  (elemTop >= docViewTop) );
	}

	$('#contents').scroll();
	

	var updateH = function(){
		if (!isScrolledIntoView($('#contents .content h1')))
		{
			$('a.top.sms').show();
			$('.help_breadcrumbs').hide();
		} else {
			$('a.top.sms').hide();
			$('.help_breadcrumbs').show();
		}
		$('#contents').css('padding-top', $('.help_breadcrumbs').outerHeight()*(7/6));
		$('a.top').css('bottom', $('#footer').outerHeight());
		$('a.top').css('left', $('#navigation').position()['left'] + (($('#navigation').outerWidth() - $('a.top').outerWidth())/2));

		$('#toc').css('top', $('#toc_border').position()['top'] + 7);

		if ($('a.top').is(':visible'))
		{
			$('#toc').css('height', $(window).height()-$('#toc').position()['top']-($(window).height() - $('a.top').position()['top']) - 10);
		} else {
			$('#toc').css('height', $(window).height()-$('#toc').position()['top']-$('#footer').outerHeight() - 20);
		}
		$('#toc').css('height', $('#toc').css('height') - 5);

		$('#toc_border').height($('#toc').outerHeight() + 5);
		$('#container #contents').css('margin-bottom', $('#footer').outerHeight());
		//$('#toc').css('top', $('#toc_border').position()['top'] + 2);
		$('#toc').css('top', $('#toc_border').position()['top'] + 7);
		$('#contents').css('right', $(window).width() - $('#navigation').position()['left'] + 5);
		//$('#toc').css('width', $('#toc_border').width() - 40);
		$('#toc').css('width', $('#toc_border').width() - 49);
	};

	var updateH_no_toc = function() {
		if (!isScrolledIntoView($('#contents .content h1')))
		{
			$('a.top.sms').show();
		} else {
			$('a.top.sms').hide();
		}
		$('a.top').css('bottom', $('#footer').outerHeight());
		
		$('#container #contents').css('margin-bottom', $('#footer').outerHeight());
	}

	if ($('body').hasClass('no-toc')) {
		updateH = updateH_no_toc;
	}
	$(window).resize(updateH);
	$('#contents').scroll(updateH);
	$(window).resize();
	
	$('a.top').click(function(){$('#contents').scrollTop(0)});

	var hashchanged = function() {
		if (window.location.hash.length) {
			openheading(window.location.hash);
			//$(window.location.hash).scrollTo();
			$(window.location.hash)[0].scrollIntoView();

		} else 
		{
			$('#contents').scrollTop(0);
		}
	};

	if (("onhashchange" in window) && !($.browser.msie)) { 
		$(window).bind( 'hashchange',hashchanged);
	}
	else { 
		var prevHash = window.location.hash;
		window.setInterval(function () {
			if (window.location.hash != prevHash) {
				hashchanged();
				prevHash = window.location.hash;
			}
		}, 100);
	}
});
