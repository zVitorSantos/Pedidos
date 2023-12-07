<template>
  <div class="container-fluid vh-100 d-flex justify-content-center align-items-center">
    <div class="register-form">
      <form class="register-container" style="width: 19rem; max-width: 100%;" @submit.prevent="handleSubmit">

        <div class="mb-4">
          <input v-model="name" type="text" id="name" class="form-control border-custom" placeholder="Nome" required pattern="[a-zA-Z]{3,}" />
        </div>

        <div class="mb-4">
          <input v-model="email" type="email" id="email" class="form-control border-custom" placeholder="Email" required />
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
            <input v-model="role" class="form-check-input" type="radio" name="role" id="client" value="client" checked />
            <label class="form-check-label" for="client">Cliente</label>
          </div>
          <div class="form-check">
            <input v-model="role" class="form-check-input" type="radio" name="role" id="representative" value="representative" />
            <label class="form-check-label" for="representative">Representante</label>
          </div>
          <div class="form-check">
            <input v-model="role" class="form-check-input" type="radio" name="role" id="employee" value="employee" />
            <label class="form-check-label" for="employee">Funcionário</label>
          </div>
          <div class="form-check">
            <input v-model="role" class="form-check-input" type="radio" name="role" id="admin" value="admin" />
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
import { ref } from 'vue';
import Notification from './Notification.vue';
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
    const role = ref('client');

    // Criar uma referência para o componente Notification
    const notificationRef = ref();

    const showNotification = (message, type = 'info') => {
      // Acessar o componente Notification usando a referência
      notificationRef.value.showNotification(message, type);
    };

    const togglePasswordVisibility = (inputId) => {
      const passwordInput = document.getElementById(inputId);

      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
      } else {
        passwordInput.type = 'password';
      }
    };

    const handleSubmit = async () => {
      if (!name.value || !email.value || !password.value || !confirmPassword.value) {
        showNotification('Por favor, preencha todos os campos.', 'error');
        return;
      }

      if (!/^[a-zA-Z ]{3,}$/.test(name.value)) {
        showNotification('Nome de usuário inválido. Deve conter no mínimo 3 letras e apenas letras ou espaços.', 'error');
        return;
      }

      const isValidEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email.value);

      if (!isValidEmail) {
        showNotification('Email inválido. Por favor, insira um email válido.', 'error');
        return;
      }

      if (password.value !== confirmPassword.value) {
        showNotification('As senhas não coincidem. Por favor, tente novamente.', 'error');
        return;
      }

      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
      if (!passwordRegex.test(password.value)) {
        showNotification('A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, uma letra minúscula e um número.', 'error');
        return;
      }

      try {
        // Fazer a requisição HTTP POST para a rota de registro
        const response = await axios.post('http://127.0.0.1:5173/api/auth/register', {
          name: name.value,
          email: email.value,
          password: password.value,
          confirmPassword: confirmPassword.value,
          role: role.value,
        });

        // Verificar se o registro foi bem-sucedido
        if (response.status === 201) {
          showNotification('Requisição de registro bem-sucedida!\nAguarde a autorização de um administrador\n para efetuar o login.', 'success');
          // Redirecionar para a página de login, se necessário
        } else {
          showNotification('Erro ao registrar. Por favor, tente novamente mais tarde.', 'error');
        }
      } catch (error) {
        console.error('Erro na requisição de registro:', error);
        showNotification('Erro ao conectar ao servidor. Por favor, tente novamente mais tarde.');
  }
};

    return {
      name,
      email,
      password,
      confirmPassword,
      role,
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
