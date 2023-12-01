<template>
  <div class="container-fluid vh-100 d-flex justify-content-center align-items-center">
    <div class="register-form">
      <form class="register-container" style="width: 19rem; max-width: 100%;" @submit.prevent="handleSubmit">

        <div class="mb-4">
          <input v-model="name" type="text" id="name" class="form-control border-custom" placeholder="Nome" required pattern="[a-zA-Z]{3,}" />
        </div>

        <div class="mb-4">
          <input v-model="email" type="email" id="email" class="form-control border-custom" placeholder="Email" required pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"/>
        </div>

        <div class="mb-4 position-relative">
          <input v-model="password" type="password" id="password" class="form-control border-custom" placeholder="Senha" />
          <i class="fas fa-eye-slash toggle-password" @click="togglePasswordVisibility('password')"></i>
        </div>

        <div class="mb-4 position-relative">
          <input v-model="confirmPassword" type="password" id="confirmPassword" class="form-control border-custom" placeholder="Repetir Senha" />
          <i class="fas fa-eye-slash toggle-password" @click="togglePasswordVisibility('confirmPassword')"></i>
        </div>

        <!-- Tipo de Usuário -->
        <div class="form-outline mb-4">
          <div class="form-check">
            <input v-model="userType" class="form-check-input" type="radio" name="userType" id="client" value="client" checked />
            <label class="form-check-label" for="client">Cliente</label>
          </div>
          <div class="form-check">
            <input v-model="userType" class="form-check-input" type="radio" name="userType" id="employee" value="employee" />
            <label class="form-check-label" for="employee">Funcionário</label>
          </div>
          <div class="form-check">
            <input v-model="userType" class="form-check-input" type="radio" name="userType" id="admin" value="admin" />
            <label class="form-check-label" for="admin">Administrador</label>
          </div>
        </div>

        <!-- Submit button -->
        <button type="button" class="btn btn-primary btn-block mb-4" @click="handleSubmit">Registrar</button>

        <!-- Register buttons -->
        <div class="text-center">
          <p>Já possui conta? <a href="/login">Entrar</a></p>
        </div>

        <Notification ref="notificationRef" />
      </form>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Notification from '../components/Notification.vue';
import axios from 'axios';

export default {
  components: {
    Notification,
  },
  setup() {
    const name = ref('');
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const userType = ref('client');

    // Criar uma referência para o componente Notification
    const notificationRef = ref();

    const showNotification = (message) => {
      // Acessar o componente Notification usando a referência
      notificationRef.value.showNotification(message);
    };

    const togglePasswordVisibility = (inputId) => {
      const passwordInput = document.getElementById(inputId);

      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
      } else {
        passwordInput.type = 'password';
      }
    };

    const handleSubmit = () => {
      if (!name.value || !email.value || !password.value || !confirmPassword.value) {
        showNotification('Por favor, preencha todos os campos.');
        return;
      }

      if (!/^[a-zA-Z]{3,}$/.test(name.value)) {
        showNotification('Nome de usuário inválido. Deve conter no mínimo 3 letras e apenas letras.');
        return;
      }

      if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email.value)) {
        showNotification('Email inválido. Por favor, insira um email válido.');
        return;
      }

      if (password.value !== confirmPassword.value) {
        showNotification('As senhas não coincidem. Por favor, tente novamente.');
        return;
      }

      // Lógica de Registro

      const registrationSucessful = true;
      if (!registrationSucessful) {
        showNotification('Erro ao registrar. Por favor, tente novamente mais tarde.');
      }
    };

    return {
      name,
      email,
      password,
      confirmPassword,
      userType,
      showNotification,
      togglePasswordVisibility,
      handleSubmit,
      notificationRef,
    };
  },
};
</script>

<style>
.container-fluid {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-form {
  height: 100%;
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.register-container {
  padding: 1rem;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 10px;
  background-color: rgb(243, 243, 243);
}

.border-custom {
  background-color: white;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 10px;
  color: rgba(128, 128, 128, 0.8);
}

.border-custom:focus,
.border-custom:valid {
  border: 1px solid rgba(128, 128, 128, 0.8);
}

.border-custom::placeholder {
  color: rgba(128, 128, 128, 0.8);
}

.toggle-password {
  cursor: pointer;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}
</style>
