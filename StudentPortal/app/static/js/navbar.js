// ---------Responsive-navbar-active-animation-----------
function test(){
	var tabsNewAnim = $('#navbarSupportedContent');
	var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
	var activeItemNewAnim = tabsNewAnim.find('.active');
	var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
	var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
	var itemPosNewAnimTop = activeItemNewAnim.position();
	var itemPosNewAnimLeft = activeItemNewAnim.position();
	$(".hori-selector").css({
		"top":itemPosNewAnimTop.top + "px", 
		"left":itemPosNewAnimLeft.left + "px",
		"height": activeWidthNewAnimHeight + "px",
		"width": activeWidthNewAnimWidth + "px"
	});
	$("#navbarSupportedContent").on("click","li",function(e){
		$('#navbarSupportedContent ul li').removeClass("active");
		$(this).addClass('active');
		var activeWidthNewAnimHeight = $(this).innerHeight();
		var activeWidthNewAnimWidth = $(this).innerWidth();
		var itemPosNewAnimTop = $(this).position();
		var itemPosNewAnimLeft = $(this).position();
		$(".hori-selector").css({
			"top":itemPosNewAnimTop.top + "px", 
			"left":itemPosNewAnimLeft.left + "px",
			"height": activeWidthNewAnimHeight + "px",
			"width": activeWidthNewAnimWidth + "px"
		});
	});
}
$(document).ready(function(){
	setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
	setTimeout(function(){ test(); }, 500);
});
$(".navbar-toggler").click(function(){
	$(".navbar-collapse").slideToggle(300);
	setTimeout(function(){ test(); });
});



// // --------------add active class-on another-page move----------
// jQuery(document).ready(function($){
// 	// Get current path and find target link
// 	var path = window.location.pathname.split("/").pop();

// 	// Account for home page with empty path
// 	if ( path == '' ) {
// 		// path = 'index.html';
//         path = "{% url 'home' %}";
// 	}

//     if ( path == 'http://127.0.0.1:8000/login/' ) {
// 		path = 'login';
      
// 	}


// 	var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
// 	// Add active class to target link
// 	target.parent().addClass('active');
// });


jQuery(document).ready(function($){
    // Get current path and find target link
    var path = window.location.pathname.split("/").pop();

    // Account for home page with empty path
    if ( path == '' ) {
        path = 'cours';
    }

    var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');

    // Add active class to target link
    target.parent().addClass('active');

    // Add links for all the pages
    var homeLink = "{% url 'accueil' %}";
    var coursesLink = "{% url 'cours' %}";
    var studentSpaceLink = "{% url 'studentSpace' %}";
    var aboutLink = "{% url 'About' %}";
    var contactLink = "{% url 'Contact' %}";
    var loginLink = "{% url 'login' %}";
    var registerLink = "{% url 'register' %}";
    var logoutLink = "{% url 'logout' %}";

    $('#navbarSupportedContent ul li a[href="'+homeLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+coursesLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+studentSpaceLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+aboutLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+contactLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+loginLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+registerLink+'"]').parent().addClass('active');
    $('#navbarSupportedContent ul li a[href="'+logoutLink+'"]').parent().addClass('active');
});





// jQuery(document).ready(function($){
//     var path = '{{ current_url }}';

//     var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
//     target.parent().addClass('active');
// });




// Add active class on another page linked
// ==========================================
// $(window).on('load',function () {
//     var current = location.pathname;
//     console.log(current);
//     $('#navbarSupportedContent ul li a').each(function(){
//         var $this = $(this);
//         // if the current path is like this link, make it active
//         if($this.attr('href').indexOf(current) !== -1){
//             $this.parent().addClass('active');
//             $this.parents('.menu-submenu').addClass('show-dropdown');
//             $this.parents('.menu-submenu').parent().addClass('active');
//         }else{
//             $this.parent().removeClass('active');
//         }
//     })
// });