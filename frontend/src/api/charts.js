import axios from "axios";
import { API_URL } from "../constants/API_URL";

export const getDebitLastMonth = () => {
	return axios.get(`${API_URL}/well_day/debit/last_mont`);
};

export const getEnergyConsumption = () => {
	return axios.get(`${API_URL}/well_day/energy_consumption`);
};
