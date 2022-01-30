<script context="module">
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    export function patchXML() {
        const csrftoken = getCookie('csrftoken');
        const originalOpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function () {
            originalOpen.apply(this, arguments);
            if (arguments[1].includes(window.location.hostname) || arguments[1].startsWith("/")) {
                this.setRequestHeader("X-CSRFToken", csrftoken);
            }
        };
    }
</script>