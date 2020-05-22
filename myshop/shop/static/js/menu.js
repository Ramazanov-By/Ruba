$(function () {
    $('.sidebar__link').each(function () {
        var location = window.location.href;
        var link = this.href;
        if(location == link) {
            $(this).addClass('sidebar__link-active');
        }
    });
});