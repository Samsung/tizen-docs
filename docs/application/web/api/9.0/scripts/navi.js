//<![CDATA[
    var staticURL = "http://img-developer.samsung.com";
   	var sslCall = "";

   	if('' !== 'N') {
		var locationStr = location.href;
		if(locationStr.indexOf("https://") > -1) {
			location.href = "http://" + locationStr.substring(8);
		}     
    }

//    	if( typeof($) === function ) {
   		//https? ??? $SD? ??? ??? https ???? http? js ???? ???? ???.
   		//? ??? ?? ?? ??? ?? ?? ???.
//    	}
    $SD.pagination.alt = {
   		first:"go first",
   		prev:"go prev",
   		next:"go next",
   		last:"go last"
    };
    $(document).ready(function(){
    	var myVar;
	    topSearchInit();//top search ??
	    $('#searchTop').attr("autocomplete","off");
	    var searchingBoolean = false;
	    
	    var topSearchChange = function(){
	    	
	    	if (searchingBoolean) return;
	    	
			var searchInput = $('#searchTop').val();
			
			if($('#searchTop').val() != ""){
				$("#topAutocomplete").hide();
				searchingBoolean = true;
				
				var jsonData = {
						url : "/search/autoComplete.do;jsessionid=hphlTh5pL0pypqhNXb18Tnhbxwzk2hBC6KxnThCvysc2Hz2WG1y2!1103778492",
						async : true,
						data : { searchInput : searchInput},
						success : function(data){
							if (searchInput == $('#searchTop').val()){
								var autoComplete = data.kwdNm;
								var tmpHtml = "";
								
								if (autoComplete.length > 0){
									$('#topAutocomplete').children().remove();
									$('#topAutocomplete').append($('<ul id="topAutocompleteList"><\/ul>'));
									$.each(autoComplete, function(i, item){
										var a = $("<a href='javascript:;'><em>"+data.searchInput+"<\/em>"+item.kwdNmSub+"<\/a>");
										a.data('keyword', item.kwdNm);
										$('#topAutocompleteList').append($('<li><\/li>').html(a));
									});
									$("#topAutocompleteList").find("li").last().on("keydown", function(e) {
										if(e.which == 9 && e.shiftKey) {
											return true;
										}
										
										if(e.which == 9) {
											e.preventDefault();
											$('#topAutocomplete').hide();	
											setTimeout(function() {
												$("#searchTopBtn").focus();
											}, 1);
										}
										
									});
									$("#searchTopBtn").off("focusout", function(e) {});
								    $("#searchTopBtn").on("focusout", function(e) {
										$('#topAutocomplete').hide();
									});
								}else{
									$('#topAutocomplete').children().remove();
								}
								if($('#searchTop').val() == ""){
									$("#topAutocomplete").hide();
									searchingBoolean = false;
									return;
								}else{
									if (searchInput == $('#searchTop').val()){
										searchingBoolean = false;
									}else{
										searchingBoolean = false;
										topSearchChange();
									}
								}
								if (autoComplete.length == 0){
									$("#topAutocomplete").hide();
								}else{
									if (searchInput == $('#searchTop').val()){
										$("#topAutocomplete").show();
										var $searchList = $("#topAutocomplete").find('ul');
										var hei = $searchList.outerHeight();
										if(hei>180){
											$searchList.css({'height':'180px','overflow-y':'auto'});
										}
									}else{
										searchingBoolean = false;
										topSearchChange();
									}
								}
							}else{
								searchingBoolean = false;
								topSearchChange();
							}
						},
						error : function() {searchingBoolean = false;}
						
				};
				//setTimeout(function(){$SD.ajax.get(jsonData);},100);
				$SD.ajax.get(jsonData);
				searchingBoolean = false;
			}
			
			//console.log("/search/autoComplete.do end");
			//console.groupEnd();
		};
		
		$('#searchTop').keyup(function(e){
			if($('#searchTop').val() == ""){
				$('#topAutocomplete').children().remove();
				$("#topAutocomplete").hide();
			}else{
				if(e.which == 13){
					search();
				}else{
					topSearchChange();
				}
			}
		});
		
		var search = function(){
			if($.trim($('#searchTop').val()) == ""){
				alert('Search keyword is required.');
			}else{
				$('#topSearchForm').submit();
			}
		};
		$("#topAutocomplete").on('mousedown','ul li a', function(e){
			e.preventDefault();
			var keyword = $(this).data('keyword');
			$("#searchTop").val(keyword);
			$('#topSearchForm').submit();
		});
		
		$("#topAutocomplete").on('keydown keypress','ul li a', function(e){
			if(e.which == 13) {
				e.preventDefault();
				var keyword = $(this).data('keyword');
				$("#searchTop").val(keyword);
				$('#topSearchForm').submit();			
			}
		});
		
		$('#searchTopBtn').click(function(e){
			search();	
		});  
    });
    
    function topSearchEnter(){
    	if($.trim($('#searchTop').val()) == "" || $.trim($('#searchTop').val()) == "Search"){
    		alert('Search keyword is required.');
    		return false;
    	}else{
    		return true;
    	}
    }

/* Tracking Code TOTAL */
		var _gaq = _gaq || [];
		var pluginUrl = '//www.google-analytics.com/plugins/ga/inpage_linkid.js';
		_gaq.push(['_require', 'inpage_linkid', pluginUrl]);
		_gaq.push(['_setAccount', 'UA-6892706-3']);
		_gaq.push(['_setDomainName', 'samsung.com']);
		_gaq.push(['_setAllowLinker', true]);
		_gaq.push(['_trackPageview']);
		(function() {
		  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		})();
	
		<!--// Tracking Code 1 -->
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-6892706-4']);
			_gaq.push(['_trackPageview']);
			(function() {
			  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			})();
