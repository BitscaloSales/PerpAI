# Create the contact page
contact_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - YashSphere AI | Book Your Demo</title>
    <meta name="description" content="Get in touch with YashSphere AI for expert contact center solutions. Book a demo, get a free migration assessment, or speak with our cloud contact center experts.">
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="icon" href="logo.png" type="image/png">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <img src="logo.png" alt="YashSphere AI" class="logo">
                <span class="logo-text">YashSphere AI</span>
            </div>
            <div class="nav-menu" id="nav-menu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="amazon-connect.html" class="nav-link">Amazon Connect</a>
                <a href="microsoft-dynamics.html" class="nav-link">Microsoft Dynamics</a>
                <a href="migrations.html" class="nav-link">Migrations</a>
                <a href="pricing.html" class="nav-link">Pricing</a>
                <a href="about.html" class="nav-link">About</a>
                <a href="resources.html" class="nav-link">Resources</a>
                <a href="contact.html" class="nav-link active">Contact</a>
                <a href="contact.html" class="btn btn-primary nav-cta">Book a Demo</a>
            </div>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero contact-hero">
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">Let's Transform Your Contact Center</h1>
                <p class="hero-description">Ready to modernize customer service with Amazon Connect or Microsoft Dynamics 365? Get a free consultation with our cloud contact center experts.</p>
            </div>
        </div>
    </section>

    <!-- Contact Methods -->
    <section class="contact-methods">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-card primary-contact">
                    <h3>Get In Touch</h3>
                    <div class="contact-info">
                        <div class="contact-item">
                            <div class="contact-icon">📧</div>
                            <div class="contact-details">
                                <strong>Email</strong>
                                <a href="mailto:Bitscalo_Sales@outlook.com">Bitscalo_Sales@outlook.com</a>
                                <small>Response within 4 hours during business hours</small>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">📞</div>
                            <div class="contact-details">
                                <strong>Phone</strong>
                                <a href="tel:+919306410903">+91-9306410903</a>
                                <small>Available Monday-Friday, 9 AM - 6 PM IST</small>
                            </div>
                        </div>
                        
                        <div class="contact-item">
                            <div class="contact-icon">🌍</div>
                            <div class="contact-details">
                                <strong>Location</strong>
                                <span>New Delhi, India</span>
                                <small>Serving clients globally with local expertise</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="contact-form-wrapper">
                    <h3>Book Your Demo</h3>
                    <p>See Amazon Connect or Microsoft Dynamics 365 in action with a personalized demo tailored to your requirements.</p>
                    
                    <form class="contact-form" netlify>
                        <div class="form-grid">
                            <div class="form-group">
                                <label for="name">Full Name *</label>
                                <input type="text" id="name" name="name" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="email">Email Address *</label>
                                <input type="email" id="email" name="email" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="company">Company Name *</label>
                                <input type="text" id="company" name="company" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="phone">Phone Number</label>
                                <input type="tel" id="phone" name="phone">
                            </div>
                            
                            <div class="form-group">
                                <label for="platform">Platform Interest</label>
                                <select id="platform" name="platform">
                                    <option value="">Select preferred platform</option>
                                    <option value="amazon-connect">Amazon Connect</option>
                                    <option value="microsoft-dynamics">Microsoft Dynamics 365</option>
                                    <option value="both">Both platforms</option>
                                    <option value="unsure">Not sure - need guidance</option>
                                </select>
                            </div>
                            
                            <div class="form-group">
                                <label for="agents">Number of Agents</label>
                                <select id="agents" name="agents">
                                    <option value="">Select range</option>
                                    <option value="1-25">1-25 agents</option>
                                    <option value="26-50">26-50 agents</option>
                                    <option value="51-100">51-100 agents</option>
                                    <option value="101-250">101-250 agents</option>
                                    <option value="250+">250+ agents</option>
                                </select>
                            </div>
                            
                            <div class="form-group full-width">
                                <label for="message">What would you like to see in the demo?</label>
                                <textarea id="message" name="message" rows="4" placeholder="Tell us about your specific use cases, integrations, or features you'd like to explore..."></textarea>
                            </div>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-large">Book Demo</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="why-choose">
        <div class="container">
            <h2 class="section-title">Why Choose YashSphere AI?</h2>
            <div class="benefits-grid">
                <div class="benefit-card">
                    <h4>Expert Implementation</h4>
                    <p>Certified specialists in both Amazon Connect and Microsoft Dynamics 365 Contact Center with proven track records.</p>
                </div>
                <div class="benefit-card">
                    <h4>Proven Results</h4>
                    <p>Successfully migrated hundreds of organizations with 99% client satisfaction and measurable business outcomes.</p>
                </div>
                <div class="benefit-card">
                    <h4>End-to-End Support</h4>
                    <p>From strategy to ongoing optimization, we're with you every step of the way with comprehensive support.</p>
                </div>
                <div class="benefit-card">
                    <h4>Industry Expertise</h4>
                    <p>Deep knowledge across fintech, healthcare, ecommerce, and BPO sectors with compliance requirements.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Response Time -->
    <section class="response-info">
        <div class="container">
            <h2 class="section-title">What to Expect</h2>
            <div class="response-grid">
                <div class="response-card">
                    <div class="response-icon">⚡</div>
                    <h4>Demo Requests</h4>
                    <p>We'll schedule your demo within 24 hours and provide a customized presentation based on your specific needs and use cases.</p>
                </div>
                <div class="response-card">
                    <div class="response-icon">💬</div>
                    <h4>General Inquiries</h4>
                    <p>Most questions answered within 4 hours during business hours (IST). Urgent matters get immediate attention.</p>
                </div>
                <div class="response-card">
                    <div class="response-icon">📊</div>
                    <h4>Migration Assessments</h4>
                    <p>Detailed assessment reports delivered within 48 hours of receiving your current system information.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="faq">
        <div class="container">
            <h2 class="section-title">Frequently Asked Questions</h2>
            
            <div class="faq-items">
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>What happens during a demo?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>We'll show you a live demonstration of either Amazon Connect or Microsoft Dynamics 365 Contact Center based on your interest. The demo is customized to your industry and use cases, typically lasting 30-45 minutes with time for Q&A.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>Is the migration assessment really free?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>Yes, completely free with no obligations. We provide a detailed analysis of your current system, migration roadmap, timeline estimates, and ROI projections to help you make an informed decision.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>Do you work with companies outside India?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>Absolutely! We serve clients globally and have experience with implementations across different time zones, compliance requirements, and regional needs.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>What information should I prepare for our conversation?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>Helpful to know: current contact center platform, number of agents, call volume, key integrations (CRM, etc.), timeline expectations, and any specific challenges you're facing. Don't worry if you don't have all details—we'll help you figure it out!</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="footer-logo">
                        <div class="nav-logo">
                            <img src="logo.png" alt="YashSphere AI" class="logo">
                            <span class="logo-text">YashSphere AI</span>
                        </div>
                        <p>Expert cloud contact center solutions for Amazon Connect and Microsoft Dynamics 365 Contact Center. From strategy to implementation, we deliver smarter customer experiences.</p>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h5>Solutions</h5>
                    <ul>
                        <li><a href="amazon-connect.html">Amazon Connect</a></li>
                        <li><a href="microsoft-dynamics.html">Microsoft Dynamics</a></li>
                        <li><a href="migrations.html">Migrations</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h5>Contact</h5>
                    <ul>
                        <li><a href="mailto:Bitscalo_Sales@outlook.com">Bitscalo_Sales@outlook.com</a></li>
                        <li><a href="tel:+919306410903">+91-9306410903</a></li>
                        <li>New Delhi, India</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 YashSphere AI. All rights reserved.</p>
                <div class="footer-links">
                    <a href="privacy.html">Privacy Policy</a>
                    <a href="terms.html">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    
    <style>
    /* Contact page specific styles */
    .contact-hero {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
        color: var(--white);
        padding: 140px 0 80px;
        text-align: center;
    }

    .contact-hero .hero-title,
    .contact-hero .hero-description {
        color: var(--white);
    }

    .contact-methods {
        padding: 100px 0;
        background: var(--gray-50);
    }

    .contact-grid {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 4rem;
        margin-top: 2rem;
    }

    .contact-card {
        background: var(--white);
        border-radius: 16px;
        padding: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        height: fit-content;
    }

    .contact-info {
        margin-top: 2rem;
    }

    .contact-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .contact-icon {
        font-size: 2rem;
        width: 50px;
        flex-shrink: 0;
    }

    .contact-details {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }

    .contact-details strong {
        color: var(--primary-blue);
        font-size: 1.1rem;
    }

    .contact-details a {
        color: var(--text-dark);
        text-decoration: none;
        font-weight: 500;
    }

    .contact-details a:hover {
        color: var(--secondary-blue);
    }

    .contact-details small {
        color: var(--text-light);
        font-size: 0.9rem;
    }

    .contact-form-wrapper {
        background: var(--white);
        border-radius: 16px;
        padding: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    }

    .contact-form-wrapper h3 {
        color: var(--primary-blue);
        margin-bottom: 1rem;
    }

    .contact-form-wrapper p {
        margin-bottom: 2rem;
    }

    .why-choose {
        padding: 100px 0;
        background: var(--white);
    }

    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }

    .benefit-card {
        padding: 2rem;
        background: var(--gray-50);
        border-radius: 12px;
        border-left: 4px solid var(--secondary-blue);
    }

    .benefit-card h4 {
        color: var(--primary-blue);
        margin-bottom: 1rem;
    }

    .response-info {
        padding: 100px 0;
        background: var(--gray-50);
    }

    .response-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }

    .response-card {
        background: var(--white);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }

    .response-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.1);
    }

    .response-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .response-card h4 {
        color: var(--primary-blue);
        margin-bottom: 1rem;
    }

    @media (max-width: 768px) {
        .contact-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        .contact-card,
        .contact-form-wrapper {
            padding: 2rem;
        }

        .benefits-grid {
            grid-template-columns: 1fr;
        }

        .response-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
</body>
</html>'''

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("✅ Created contact.html")