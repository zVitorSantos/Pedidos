<template>
  <div class="container-fluid vh-100 d-flex justify-content-center align-items-center">
    <div class="login-form">
      <form class="login-container" style="width: 19rem; max-width: 100%;" @submit.prevent="handleSubmit">

        <div class="mb-4">
          <input v-model="email" type="email" id="email" class="form-control border-custom" placeholder="Email" />
        </div>

        <div class="mb-4 position-relative">
          <input v-model="password" type="password" id="password" class="form-control border-custom" placeholder="Senha" />
          <i class="fas fa-eye-slash toggle-password" @click="togglePasswordVisibility"></i>
        </div>

        <div class="row mb-4">
          <div class="col d-flex justify-content-center">
            <div class="form-check">
              <input v-model="rememberMe" class="form-check-input" type="checkbox" value="" id="remember" checked @change="handleRememberMeChange" />
              <label class="form-check-label" for="remember">Lembre-me</label>
            </div>
          </div>

          <div class="col">
            <!-- Simple link -->
            <a href="#!">Esqueceu a senha?</a>
          </div>
        </div>

        <!-- Submit button -->
        <button type="submit" class="btn btn-primary btn-block mb-4">Entrar</button>

        <!-- Register buttons -->
        <div class="text-center">
          <p>Não possui conta? <a href="/register">Pedir Acesso</a></p>
        </div>

        <!-- Incorporando o componente de notificação -->
        <Notification ref="notification" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import Notification from './Notification.vue';

let email = '';
let password = '';
let rememberMe = true;

const notification = ref(null);

function showNotification(message, type = 'info') {
  notification.value.showNotification(message, type);
}

function handleRememberMeChange() {
  if (rememberMe) {
    // Emita um token de atualização de longa duração
    authService.issueRefreshToken(user, '7d');  // 7 dias
  } else {
    // Emita um token de atualização de curta duração
    authService.issueRefreshToken(user, '1h');  // 1 hora
  }
}

// Função para alternar a visibilidade da senha
function togglePasswordVisibility() {
  const passwordInput = document.getElementById('password');
  const icon = document.querySelector('.toggle-password');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
  } else {
    passwordInput.type = 'password';
    icon.classList.remove('fa-eye');
    icon.classList.add('fa-eye-slash');
  }
}

async function handleSubmit() {
  // Verifique se os campos estão preenchidos
  if (!email || !password) {
    showNotification('Por favor, preencha todos os campos.', 'error');
    return;
  }

  try {
    // Faça uma solicitação POST para a rota de login
    const response = await axios.post('http://127.0.0.1:5173/api/auth/login', {
      email,
      password,
      rememberMe,  // Adicione a opção "Lembre-me" ao corpo da solicitação
    });

    // Se a solicitação for bem-sucedida, armazene o token de acesso e o token de atualização no local storage
    localStorage.setItem('accessToken', response.data.access_token);
    localStorage.setItem('refreshToken', response.data.refresh_token);

    // Redirecione o usuário para a página inicial após um pequeno atraso
    setTimeout(() => {
      window.location.href = '/';
    }, 100);
  } 
  catch (error) {
    if (error.response) {
      // O pedido foi feito e o servidor respondeu com um status fora do intervalo de 2xx
      if (error.response.status === 401) {
        showNotification('Erro ao fazer login. Verifique suas credenciais.', 'error');
      } else {
        showNotification('Erro no servidor. Por favor, tente novamente mais tarde.', 'error');
      }
    } else if (error.request) {
      // O pedido foi feito, mas nenhuma resposta foi recebida
      showNotification('Erro de rede. Por favor, verifique sua conexão com a internet.', 'error');
    } else {
      // Algo aconteceu na configuração do pedido que acionou um erro
      showNotification('Erro ao fazer login. Por favor, tente novamente mais tarde.', 'error');
    }
  }
}
</script>

<style>
.container-fluid {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-form {
  height: 100%;
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-container {
  padding: 1rem;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 5px;
  background-color: rgb(243, 243, 243);
}

.border-custom {
  background-color: white;
  border: 1px solid rgba(128, 128, 128, 0.8);
  border-radius: 5px;
  color: rgba(128, 128, 128, 0.8);
}

.border-custom:focus,
.border-custom:valid {
  border: 1px solid rgba(128, 128, 128, 0.8);
}

.border-custom::placeholder {
  color: rgba(128, 128, 128, 0.8);
}

.row .col {
  padding-left: 0;
  padding-right: 0;
}

.toggle-password {
  cursor: pointer;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background-color: white; 
  padding: 5px;
}
</style>