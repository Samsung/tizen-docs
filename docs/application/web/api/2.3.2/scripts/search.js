/** 
 * [PAGE] Search Result
 * date : 20120810
 * author : 전종호
 */
function searchInit()
{
	var focusTarget = "input";

	//$("#autocomplete").hide();

	//$("#searchInput").bind("keydown", checkSearchText);
	
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
	
	$("#autocomplete").bind("mouseleave",function(){
		$(this).hide();
		$("#btnDropdown").removeClass("dropdownoff");
		$("#btnDropdown").addClass("dropdown");		
	});

	$(".autocomplete ul li:last-child").focusout( function() {
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
			//$(".autocomplete").css("visibility", "visible");
			$("#autocomplete").show();
			
			$("#btnDropdown").removeClass("dropdown");
			$("#btnDropdown").addClass("dropdownoff");
		}
		else{
			//$(".autocomplete").css("visibility", "hidden");
			$("#autocomplete").hide();
			
			$("#btnDropdown").removeClass("dropdownoff");
			$("#btnDropdown").addClass("dropdown");
		}
	}
}



function topSearchInit()
{
	var focusTarget = "input";

	//$("#searchTop").bind("keydown", checkSearchText);
	
	$("#searchTop").focusout(function() {
		if( focusTarget == "dropdown" )
		{
			return false;
		}
		else
		{	
			//toggleClass( false );
		}
	});
	
	$( "#searchTop" ).focusin( function()	{
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
			var txt = $("#searchTop").val();

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
			$(".topAutocomplete").css("visibility", "visible");
		}else{
			$(".topAutocomplete").css("visibility", "hidden");
			$("#topAutocomplete").hide();
		}
	}
}
