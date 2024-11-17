import axios from "axios";
import { API_URL } from "../constants/API_URL";

export const getEnergyIntensiveTop = () => {
	return axios.get(`${API_URL}/well_day/most_ee_wells`);
};

export const getMostPerfomance = () => {
	return axios.get(`${API_URL}/well_day/most_perfomance`);
};
