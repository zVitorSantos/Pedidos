<template>
    <div>
        <NavBarAuth />
        
        <Config />

        <Footer />
    </div>
</template>

<script>
import NavBarAuth from "../components/NavBarAuth.vue";
import Config from "../components/Settings.vue";
import Footer from "../components/Footer.vue";

export default {
    name: "Config",
    components: {
        NavBarAuth,
        Footer,
    },
    beforeRouteEnter(to, from, next) {
        // Check if the user is authorized
        if (!isAuthorized()) {
            next("/login");
        } else {
            next();
        }
    },
};

function isAuthorized() {
    // Implement your authorization logic here
    // Return true if the user is authorized, false otherwise
}
</script>

<style>
/* Add your custom styles here */
</style>
