import React from 'react';
import { Button } from '../components/atoms/Button';
import { useAuth } from '../hooks/useAuth';

const Dashboard: React.FC = () => {
  const { logout } = useAuth();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-2xl w-full max-w-md">
        <h1 className="text-3xl font-bold mb-6 text-center">
          Welcome to Ventry Dashboard
        </h1>
        <p className="text-gray-600 mb-6 text-center">
          You have successfully logged in!
        </p>
        <Button
          variant="secondary"
          onClick={logout}
        >
          Logout
        </Button>
      </div>
    </div>
  );
};

export default Dashboard;
