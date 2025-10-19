import { FiCamera, FiClock, FiUsers, FiZap, FiEdit, FiCheck } from "react-icons/fi";

import { IBenefit } from "@/types"

export const benefits: IBenefit[] = [
    {
        title: "The Process",
        description: "Effortless. Precise. Beautiful. From photo to fashion story — perfected within a day.",
        bullets: [
            {
                title: "You Send the Look",
                description: "A photo of your garment is all we need to get started.",
                icon: <FiCamera size={26} />
            },
            {
                title: "AI Creates the Vision",
                description: "Crafted by our expert prompt engineers for stunning results.",
                icon: <FiZap size={26} />
            },
            {
                title: "Editors Refine the Detail",
                description: "Every pixel perfected by our human editors.",
                icon: <FiEdit size={26} />
            }
        ],
        imageSrc: "/images/mockup-1.webp"
    },
    {
        title: "Why It Works",
        description: "We merge couture with code. Our AI pipeline + human editors deliver imagery worthy of the glossiest covers.",
        bullets: [
            {
                title: "Exceptional Results at a Fraction of the Cost",
                description: "Professional quality without the professional price tag.",
                icon: <FiCheck size={26} />
            },
            {
                title: "Turnaround That Matches Your Pace",
                description: "Within 24 hours — or it's on us.",
                icon: <FiClock size={26} />
            },
            {
                title: "Limitless Looks, Diverse Models, Every Aesthetic",
                description: "Zero logistics, zero risk — only perfection delivered.",
                icon: <FiUsers size={26} />
            }
        ],
        imageSrc: "/images/mockup-2.webp"
    },
    {
        title: "Where You Shine",
        description: "Our promise: No studios. No shipping. No stress. Just pure, editorial-grade imagery at scale.",
        bullets: [
            {
                title: "Product Listings That Convert",
                description: "Transform flat lays into compelling lifestyle imagery.",
                icon: <FiCamera size={26} />
            },
            {
                title: "Social Campaigns That Stop the Scroll",
                description: "Create content that demands attention on every platform.",
                icon: <FiZap size={26} />
            },
            {
                title: "Digital Catalogues for Global Launches",
                description: "Influencer-style looks without the logistics.",
                icon: <FiUsers size={26} />
            }
        ],
        imageSrc: "/images/mockup-1.webp"
    },
]