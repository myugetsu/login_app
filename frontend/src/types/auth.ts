export interface UserCredentials {
  email: string;
  password: string;
}

export interface SignupData extends UserCredentials {
  fullName: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}
