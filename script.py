# Create the complete YashSphere AI website with all files
import os

# Create a comprehensive index.html file
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YashSphere AI - Cloud Contact Center Experts | Amazon Connect & Microsoft Dynamics 365</title>
    <meta name="description" content="Expert cloud contact center solutions for Amazon Connect and Microsoft Dynamics 365. From strategy to implementation, we deliver smarter customer experiences.">
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
                <a href="index.html" class="nav-link active">Home</a>
                <a href="amazon-connect.html" class="nav-link">Amazon Connect</a>
                <a href="microsoft-dynamics.html" class="nav-link">Microsoft Dynamics</a>
                <a href="migrations.html" class="nav-link">Migrations</a>
                <a href="pricing.html" class="nav-link">Pricing</a>
                <a href="about.html" class="nav-link">About</a>
                <a href="resources.html" class="nav-link">Resources</a>
                <a href="contact.html" class="nav-link">Contact</a>
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
    <section class="hero">
        <div class="hero-bg">
            <img src="hero-bg.png" alt="Contact Center" class="hero-image">
            <div class="hero-overlay"></div>
        </div>
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">Cloud Contact Center Experts</h1>
                <p class="hero-subtitle">Smarter Contact Centers. Simpler Operations.</p>
                <p class="hero-description">We design, implement, and optimize Amazon Connect and Microsoft Dynamics 365 Contact Center solutions. From discovery to deployment—fewer phone trees, more first-contact resolutions.</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="btn btn-primary btn-large">Book a Demo</a>
                    <a href="contact.html" class="btn btn-secondary btn-large">Free Migration Assessment</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Two Platform Solutions -->
    <section class="solutions">
        <div class="container">
            <h2 class="section-title">Two Best-in-Class Solutions</h2>
            <p class="section-subtitle">Choose the platform that fits your ecosystem. We deliver end-to-end implementation for both.</p>
            
            <div class="solutions-grid">
                <div class="solution-card">
                    <div class="solution-icon">
                        <img src="aws-icon.png" alt="Amazon Connect" class="platform-icon">
                    </div>
                    <h3>Amazon Connect</h3>
                    <p class="solution-subtitle">AWS Native Contact Center</p>
                    <ul class="solution-features">
                        <li>Infinite scalability with AWS infrastructure</li>
                        <li>Contact Lens AI for real-time insights</li>
                        <li>Pay-per-use pricing model</li>
                        <li>Native AWS service integrations</li>
                        <li>Advanced omnichannel routing</li>
                    </ul>
                    <div class="solution-buttons">
                        <a href="amazon-connect.html" class="btn btn-outline">Learn More</a>
                        <a href="contact.html" class="btn btn-primary">Book Demo</a>
                    </div>
                </div>

                <div class="solution-card">
                    <div class="solution-icon">
                        <img src="ms-icon.png" alt="Microsoft Dynamics 365" class="platform-icon">
                    </div>
                    <h3>Microsoft Dynamics 365</h3>
                    <p class="solution-subtitle">Contact Center</p>
                    <ul class="solution-features">
                        <li>Deep Microsoft 365 integration</li>
                        <li>Copilot AI assistance for agents</li>
                        <li>Unified case management</li>
                        <li>Power Platform automation</li>
                        <li>Teams native experience</li>
                    </ul>
                    <div class="solution-buttons">
                        <a href="microsoft-dynamics.html" class="btn btn-outline">Learn More</a>
                        <a href="contact.html" class="btn btn-primary">Book Demo</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Business Outcomes -->
    <section class="outcomes">
        <div class="container">
            <h2 class="section-title">Proven Business Outcomes</h2>
            <p class="section-subtitle">Our clients see measurable improvements within the first quarter</p>
            
            <div class="outcomes-grid">
                <div class="outcome-card">
                    <div class="outcome-number">40%</div>
                    <h4>Faster Resolution</h4>
                    <p>Reduce average handling time with smart routing</p>
                </div>
                <div class="outcome-card">
                    <div class="outcome-number">25%</div>
                    <h4>Higher CSAT</h4>
                    <p>Deliver exceptional customer experiences</p>
                </div>
                <div class="outcome-card">
                    <div class="outcome-number">30%</div>
                    <h4>Lower Costs</h4>
                    <p>Optimize operations and reduce overhead</p>
                </div>
                <div class="outcome-card">
                    <div class="outcome-number">50%</div>
                    <h4>Better Agent Productivity</h4>
                    <p>Empower agents with AI-powered tools</p>
                </div>
            </div>
        </div>
    </section>

    <!-- How We Work -->
    <section class="process">
        <div class="container">
            <h2 class="section-title">How We Work</h2>
            <p class="section-subtitle">A proven methodology that delivers results</p>
            
            <div class="process-steps">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <h4>Discover</h4>
                    <p>Assess current state and define requirements</p>
                </div>
                <div class="process-step">
                    <div class="step-number">2</div>
                    <h4>Design</h4>
                    <p>Architect the optimal solution for your needs</p>
                </div>
                <div class="process-step">
                    <div class="step-number">3</div>
                    <h4>Implement</h4>
                    <p>Deploy with minimal disruption to operations</p>
                </div>
                <div class="process-step">
                    <div class="step-number">4</div>
                    <h4>Optimize</h4>
                    <p>Continuous improvement and managed services</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Integrations -->
    <section class="integrations">
        <div class="container">
            <h2 class="section-title">Seamless Integrations</h2>
            <p class="section-subtitle">Connect with your existing tools and workflows</p>
            
            <div class="integration-logos">
                <div class="integration-item">Salesforce</div>
                <div class="integration-item">HubSpot</div>
                <div class="integration-item">Zendesk</div>
                <div class="integration-item">Freshdesk</div>
                <div class="integration-item">WhatsApp</div>
                <div class="integration-item">Microsoft 365</div>
                <div class="integration-item">Power Platform</div>
                <div class="integration-item">Service Hub</div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials">
        <div class="container">
            <h2 class="section-title">What Our Clients Say</h2>
            
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <p>"YashSphere AI transformed our contact center in just eight weeks. The migration was seamless and our CSAT scores improved by 30%."</p>
                    </div>
                    <div class="testimonial-author">
                        <h5>Sarah Johnson</h5>
                        <span>VP of Customer Experience, TechCorp</span>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <p>"Finally, a partner who understands both the technical and business aspects of contact center transformation."</p>
                    </div>
                    <div class="testimonial-author">
                        <h5>Michael Chen</h5>
                        <span>IT Director, Finance First</span>
                    </div>
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
                        <h4>How long does a typical migration take?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>SMB implementations typically take 4-8 weeks, while enterprise deployments range from 12-20 weeks depending on complexity.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>What about security and compliance?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>Both Amazon Connect and Microsoft Dynamics 365 Contact Center meet SOC2, GDPR, and industry-specific compliance requirements. We ensure secure data migration and ongoing compliance.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>Which platform is right for us?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>Amazon Connect excels for AWS-native organizations, while Microsoft Dynamics 365 Contact Center is ideal for Microsoft 365 environments. We'll help you choose based on your ecosystem.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFAQ(this)">
                        <h4>How do you approach pricing?</h4>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        <p>We offer value-based pricing tied to your business outcomes with transparent project scoping and no hidden fees.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <h2>Ready to Transform Your Contact Center?</h2>
            <p>Join hundreds of companies who've modernized their customer experience with YashSphere AI</p>
            <a href="contact.html" class="btn btn-primary btn-large">Book a Demo</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="footer-logo">
                        <img src="logo.png" alt="YashSphere AI" class="logo">
                        <span class="logo-text">YashSphere AI</span>
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
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("✅ Created index.html")