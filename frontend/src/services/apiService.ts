import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; //llamando a la API de django

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
    order: number;
    is_featured: boolean;
}

export interface TeamMember {
  id: number;
  name: string;
  position: string;
  bio: string;
  photo: string; 
  linkedin_url: string;
  order: number;
  is_partner: boolean;
}

interface PaginatedResponse<T> {
    count: number;
    next: string | null;
    previous: string | null;
    results: T[];
}

export default {
    async fetchServices(): Promise<Service[]> {
        const response = await apiClient.get<PaginatedResponse<Service>>('/services/');
        return response.data.results;  // ← Solo devuelve los results
    },

    async fetchTeamMembers(): Promise<TeamMember[]> {
        const response = await apiClient.get<PaginatedResponse<TeamMember>>('/team/');
        return response.data.results;  // ← Solo devuelve los results
    }
}