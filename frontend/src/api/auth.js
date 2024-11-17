import axios from "axios";
import { API_URL } from "../constants/API_URL";

export const loginUser = (login, password) => {
	return axios.post(`${API_URL}/auth/login`, { login, password });
};

export const refreshUser = () => {
	return axios.post(`${API_URL}/auth/refresh`);
};

export const logoutUser = () => {
	return axios.post(`${API_URL}/auth/logout`);
};
