<template>
    <div v-if="isVisible" class="notification">
      {{ message }}
    </div>
</template>

<script>
export default {
data() {
    return {
    isVisible: false,
    message: '',
    };
},
methods: {
    showNotification(message) {
    this.isVisible = true;
    this.message = message;

    setTimeout(() => {
        this.hideNotification();
    }, 3000);
    },
    hideNotification() {
    this.isVisible = false;
    this.message = '';
    },
},
};
</script>

<style scoped>
.notification {
position: fixed;
top: 20px; 
left: 50%;
transform: translateX(-50%);
padding: 10px;
background-color: #ff0000d7; 
color: #fff; 
z-index: 1000;
border: 1px solid black;
border-radius: 10px; 
}
</style>
