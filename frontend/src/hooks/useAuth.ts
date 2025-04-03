import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authService, SignupData } from '../services/auth.service';

export const useAuth = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const login = async (email: string, password: string) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await authService.login(email, password);
      localStorage.setItem('token', response.access_token);
      navigate('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Login failed');
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const signup = async (data: SignupData) => {
    setIsLoading(true);
    setError(null);

    try {
      await authService.signup(data);
      await login(data.email, data.password);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Signup failed');
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const verifyAccessCode = async (code: string): Promise<boolean> => {
    return await authService.verifyAccessCode(code);
  };

  const logout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const isAuthenticated = (): boolean => {
    const token = localStorage.getItem('token');
    return !!token; // Convert to boolean
  };

  return {
    login,
    signup,
    logout,
    verifyAccessCode,
    isAuthenticated,
    isLoading,
    error
  };
};
