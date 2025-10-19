import { IPricing } from "@/types";

export const tiers: IPricing[] = [
    {
        name: 'Starter',
        price: '₹2,500',
        features: [
            'Up to 10 images',
            'AI-generated models & styling',
            'Human editor refinement',
            '24-hour delivery guarantee',
            'High-resolution output',
            'Email support',
        ],
    },
    {
        name: 'Growth',
        price: '₹7,500',
        features: [
            'Up to 30 images',
            'AI-generated models & styling',
            'Human editor refinement',
            '24-hour delivery guarantee',
            'High-resolution output',
            'Brand aesthetic matching',
            'Priority support',
        ],
    },
    {
        name: 'Professional',
        price: '₹18,000',
        features: [
            'Up to 75 images',
            'AI-generated models & styling',
            'Human editor refinement',
            '24-hour delivery guarantee',
            'High-resolution output',
            'Brand aesthetic matching',
            'Multiple style variations',
            'Dedicated account manager',
        ],
    },
    {
        name: 'Enterprise',
        price: '₹28,800',
        features: [
            'Up to 120 images',
            'AI-generated models & styling',
            'Human editor refinement',
            '24-hour delivery guarantee',
            'High-resolution output',
            'Brand aesthetic matching',
            'Multiple style variations',
            'Dedicated account manager',
            'Custom model training',
            'White-label options',
        ],
    },
]