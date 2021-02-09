$( document ).ready(function() {

$(window).scroll(function(){
     var topPage = $('html').scrollTop();
     var headerHeight = $('header').height();

        $('header > h1').css("opacity", (-((topPage - headerHeight) / 150)+1.22));

});
});