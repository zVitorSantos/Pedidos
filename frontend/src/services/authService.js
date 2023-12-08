import axios from 'axios';

const authService = {
  login: async (email, password) => {
    const response = await axios.post('/api/auth/login', { email, password });
    return response.data;
  },
  logout: async () => {
    const response = await axios.post('/api/auth/logout');
    return response.data;
  },
  register: async (data) => {
    const response = await axios.post('/api/auth/register', data);
    return response.data;
  },
  approveUser: async (userId, data) => {
    const response = await axios.post(`/api/auth/approve_user/${userId}`, data);
    return response.data;
  },
  rejectUser: async (userId) => {
    const response = await axios.post(`/api/auth/reject_user/${userId}`);
    return response.data;
  },
  getPendingUsers: async () => {
    const response = await axios.get('/api/auth/pending_users');
    return response.data;
  },
  verifyToken: async () => {
    const response = await axios.get('/api/auth/verify-token');
    return response.data;
  },
  refreshToken: async () => {
    const response = await axios.post('/api/auth/refresh');
    return response.data;
  },
};

export default authService;