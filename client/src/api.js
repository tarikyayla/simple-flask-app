import axios from 'axios';

export const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
export const BASE_URL = process.env.REACT_APP_BASE_URL;

export const apiInstance = axios.create({
  baseURL: BACKEND_URL,
  headers: {
    'Access-Control-Allow-Origin': '*',
  },
});

export const get_location = ({ id }) => apiInstance.get(`/locations/${id}`);
export const get_locations = ({ page, items_per_page }) =>
  apiInstance.get(`/locations?page=${page}&items-per-page=${items_per_page}`);
export const get_switch = ({ id }) => apiInstance.get(`/switches/${id}`);
export const get_switches = ({ id, page, items_per_page }) =>
  apiInstance.get(
    `/locations/${id}/switches?page=${page}&items-per-page=${items_per_page}`
  );

export const get_ports = ({ id, page, items_per_page }) =>
  apiInstance.get(
    `/switches/${id}/ports?page=${page}&items-per-page=${items_per_page}`
  );
