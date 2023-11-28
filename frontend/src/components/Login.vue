<template>
    <div class="container mt-5 d-flex justify-content-center align-items-center">
      <div class="login-form" style="max-width: 30%;">
        <form>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <input type="email" id="email" class="form-control border-custom" />
            <label class="form-label" for="email">Endereço de Email</label>
          </div>
  
          <!-- Password input -->
          <div class="form-outline mb-4">
            <input type="password" id="password" class="form-control border-custom" />
            <label class="form-label" for="password">Senha</label>
          </div>
  
          <!-- 2 column grid layout for inline styling -->
          <div class="row mb-4">
            <div class="col d-flex justify-content-center">
              <!-- Checkbox -->
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="remember" checked />
                <label class="form-check-label" for="remember"> Me Lembre </label>
              </div>
            </div>
  
            <div class="col">
              <!-- Simple link -->
              <a href="#!">Esqueceu a senha?</a>
            </div>
          </div>
  
          <!-- Submit button -->
          <button type="button" class="btn btn-primary btn-block mb-4">Sign in</button>
  
          <!-- Register buttons -->
          <div class="text-center">
            <p>Não possúi conta? <a href="/register">Pedir Acesso</a></p>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <style>
  .login-form {
    height: 100%;
    width: 100%;
    max-width: 400px;
    margin: auto;
  }
  
  /* Aumentando a especificidade para a classe border-custom */
  .form-outline .border-custom {
    border: 1px solid ;
    border-radius: 5px;
  }
  </style>