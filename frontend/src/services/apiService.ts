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

export interface TeamMember {
  id: number;
  name: string;
  position: string;
  bio: string;
  photo: string; // La URL de la foto
  linkedin_url: string;
  is_partner: boolean;
}

export interface CarouselSlide {
  id: number;
  title: string;
  subtitle: string;
  image: string;
  link_text: string;
  link_url: string;
}

export default {
    fetchServices(): Promise<{ results: Service[] }> {
        return apiClient.get('/services/').then(response => response.data);
    },

    fetchTeamMembers(): Promise<{results: TeamMember[]}> {
        return apiClient.get('/team/').then(response => response.data);
    },

    fetchCarouselSlides(): Promise<{results: CarouselSlide[]}> {
        return apiClient.get('/carousel-slides/').then(response => response.data);
    }
}