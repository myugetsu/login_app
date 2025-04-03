import React from 'react';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  className,
  ...props
}) => {
  return (
    <div className="w-full">
      {label && (
        <label className="block mb-2 text-sm font-medium text-gray-700">
          {label}
        </label>
      )}
      <input
        className={`
          w-full
          px-4
          py-2
          border
          rounded-lg
          focus:outline-none
          focus:ring-2
          focus:ring-black
          ${className}
        `}
        {...props}
      />
    </div>
  );
};
