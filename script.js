document.addEventListener("DOMContentLoaded", function () {
    if (window.Telegram && Telegram.WebApp) {
        let user = Telegram.WebApp.initDataUnsafe.user;
        let theme = Telegram.WebApp.themeParams;

        if (user) {
            document.getElementById("username").textContent = user.first_name + " " + (user.last_name || "");
        }

        // اعمال تم تلگرام به عناصر صفحه
        document.body.style.setProperty('--tg-theme-bg-color', theme.bg_color || '#121212');
        document.body.style.setProperty('--tg-theme-text-color', theme.text_color || '#ffffff');
        document.body.style.setProperty('--tg-theme-hint-color', theme.hint_color || '#b0b0b0');
        document.body.style.setProperty('--tg-theme-button-color', theme.button_color || '#008c9e');
        document.body.style.setProperty('--tg-theme-button-text-color', theme.button_text_color || '#ffffff');
        document.body.style.setProperty('--tg-theme-link-color', theme.link_color || '#00bcd4');
    }
});