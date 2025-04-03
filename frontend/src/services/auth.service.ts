import axiosInstance from './utils/axiosInstance';

export interface SignupData {
  email: string;
  password: string;
  fullName: string;
}

export const authService = {
  async login(email: string, password: string) {
    const response = await axiosInstance.post(`/login`,
      new URLSearchParams({
        username: email,
        password: password
      }),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
    return response.data;
  },

  async signup(data: SignupData) {
    const response = await axiosInstance.post(`/signup`, {
      email: data.email,
      password: data.password,
      full_name: data.fullName
    });
    return response.data;
  },

  async verifyAccessCode(code: string): Promise<boolean> {
    try {
      const response = await axiosInstance.post(`/verify-access-code`, {
        access_code: code
      });
      return response.status === 200;
    } catch {
      return false;
    }
  },
};
