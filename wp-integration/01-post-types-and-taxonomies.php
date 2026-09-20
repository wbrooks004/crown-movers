<?php
/**
 * Crown Movers — Phase 1 post types & taxonomies.
 *
 * Source of truth: Crown_Movers_Content_Architecture_Spec_v2.md §3.1, §3.5, §4
 * (most recently modified Drive copy, 2026-07-30T21:37 — diffed against the
 * other saved copy, content identical on every point this file implements).
 *
 * Install as a must-use plugin (wp-content/mu-plugins/) or a small standalone
 * plugin. Do NOT register a `service` CPT here — Phase 1 keeps services as
 * Pages + the Service field group (see 02-acf-field-groups.php); a service
 * CPT is explicitly listed as "deliberately not created" in Phase 1 (§3.5),
 * gated behind the service-URL decision in §6.3.
 *
 * Manual step this file cannot do: enable both `location` and `service_category`
 * for translation under Polylang → Languages → Settings → Custom Post Types and
 * Taxonomies. That toggle is Polylang UI only.
 *
 * Before this goes live, run the staging test matrix in the spec (§10.4) —
 * the rewrite/query-var change below is flagged there as the risk item.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * location — service-area pages (§3.1).
 *
 * Empty rewrite slug preserves existing URLs (/laval-movers/,
 * /fr/demenagement-laval/, ...) unchanged, per the spec's Phase 1 rule of
 * zero URL changes. has_archive is false on purpose: the "areas we serve"
 * hub is a designed Page (bricks/11-archive-location.json), not a CPT
 * archive route — a true archive route would collide with the empty-slug
 * namespace Pages already occupy.
 */
add_action( 'init', function () {
	register_post_type( 'location', [
		'labels' => [
			'name'          => __( 'Locations', 'crown-movers' ),
			'singular_name' => __( 'Location', 'crown-movers' ),
			'add_new_item'  => __( 'Add New Location', 'crown-movers' ),
			'edit_item'     => __( 'Edit Location', 'crown-movers' ),
			'all_items'     => __( 'Locations', 'crown-movers' ),
		],
		'public'       => true,
		'hierarchical' => false,
		'has_archive'  => false,
		'rewrite'      => [ 'slug' => '', 'with_front' => false ],
		'supports'     => [ 'title', 'editor', 'thumbnail', 'excerpt', 'revisions', 'custom-fields' ],
		'show_in_rest' => true,
		'menu_icon'    => 'dashicons-location',
	] );
} );

/**
 * region — groups the ~267 location posts (§4). Hierarchical; taxonomy terms
 * translate on Polylang Free (unlike CPT rewrite bases), which is why the
 * spec routes area-grouping and internal linking through this taxonomy
 * instead of an ACF relationship field (§7.3).
 *
 * Set initial terms to Crown Movers' actual coverage only — do not add a
 * term for an area the company does not serve. Starting set per §4:
 * Montreal Island, West Island, Laval, South Shore (Rive-Sud),
 * North Shore (Rive-Nord), Laurentians, Outside Greater Montreal.
 */
add_action( 'init', function () {
	register_taxonomy( 'region', [ 'location' ], [
		'labels'            => [ 'name' => __( 'Regions', 'crown-movers' ) ],
		'hierarchical'      => true,
		'public'            => true,
		'show_in_rest'      => true,
		'show_admin_column' => true,
		'rewrite'           => false,
	] );
} );

add_action( 'init', function () {
	$regions = [ 'Montreal Island', 'West Island', 'Laval', 'South Shore (Rive-Sud)', 'North Shore (Rive-Nord)', 'Laurentians', 'Outside Greater Montreal' ];
	foreach ( $regions as $region ) {
		if ( ! term_exists( $region, 'region' ) ) {
			wp_insert_term( $region, 'region' );
		}
	}
}, 20 );

/**
 * service_category — classifies which Pages are service pages, and groups
 * them for breadcrumbs/filtering/serviceType (§4). Applied to `page`, not a
 * CPT — see file header. Non-hierarchical by spec.
 *
 * bricks/12-single-service.json's single-service Bricks template targets
 * `templateConditions: [{"main":"terms","terms":["service_category::all"]}]`
 * — i.e. any Page carrying ANY term in this taxonomy. bricks/10-archive-service.json's
 * services-listing loop filters page posts where this taxonomy EXISTS. Both
 * require every service Page to be tagged with at least one term here.
 */
add_action( 'init', function () {
	register_taxonomy( 'service_category', [ 'page' ], [
		'labels'            => [ 'name' => __( 'Service Category', 'crown-movers' ) ],
		'hierarchical'      => false,
		'public'            => true,
		'show_in_rest'      => true,
		'show_admin_column' => true,
		'rewrite'           => false,
	] );
} );

add_action( 'init', function () {
	$categories = [ 'Residential', 'Commercial', 'Specialty', 'Packing & Assembly', 'Storage', 'Long-Distance', 'Junk Removal' ];
	foreach ( $categories as $category ) {
		if ( ! term_exists( $category, 'service_category' ) ) {
			wp_insert_term( $category, 'service_category' );
		}
	}
}, 20 );

/**
 * "Service" page template — deliberately virtual (no physical .php file).
 * It exists only so:
 *   1. editors get a labeled "Service" choice in Page Attributes, and
 *   2. the ACF Service field group (02-acf-field-groups.php) can target it
 *      via ACF's native "Page Template" location rule.
 *
 * This is NOT what routes the Bricks frontend template: Bricks 2.3.6 has no
 * "Page Template" templateCondition (verified against includes/templates.php),
 * so bricks/12-single-service.json targets the service_category taxonomy
 * instead (see above). A service page therefore needs both set by the editor:
 * this template (admin marker + field visibility) and a service_category
 * term (what Bricks and the listing loop actually key off). Because no file
 * named crown-service-template.php exists, WordPress silently falls back to
 * the normal page template hierarchy for anything else that reads it —
 * Bricks' own template_include override is what actually renders the page.
 */
add_filter( 'theme_page_templates', function ( $templates ) {
	$templates['crown-service-template.php'] = __( 'Service', 'crown-movers' );
	return $templates;
} );

/**
 * Option A from the spec (§3.1): because location's rewrite base is empty,
 * a name-only request like /laval-movers/ doesn't resolve to the CPT without
 * help — WordPress only checks pages and posts by default. This widens the
 * front-end main query's post_type so it also checks `location`.
 *
 * [VERIFICATION REQUIRED — staging, per spec §10.4] Run the full test matrix
 * before this goes live: a genuine 404 must still 404, no page/location slug
 * may collide, paginated archives and the blog index must still resolve.
 */
add_action( 'pre_get_posts', function ( $query ) {
	if ( is_admin() || ! $query->is_main_query() ) {
		return;
	}
	if ( $query->get( 'pagename' ) !== '' || $query->get( 'name' ) !== '' ) {
		$query->set( 'post_type', [ 'page', 'post', 'location' ] );
	}
} );
