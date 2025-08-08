import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type':'application/json',
    },
});

export interface Service {
    id: number;
    title: string;
    slug: string;
    short_description: string;
    description: string;
    icon: string;
    is_featured: boolean;
}

export default {
    fetchServices(): Promise<{ results: Service[] }> {
        return apiClient.get('/services/').then(response => response.data);
    }
}